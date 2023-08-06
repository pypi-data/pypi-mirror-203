# ruff: noqa: E501

from __future__ import annotations

__all__ = ["Queue"]

import logging
from asyncio import sleep
from random import randint
from typing import Self
from arq.connections import ArqRedis, create_pool
from arq.jobs import JobDef

from .config import QueueSettings
from .exceptions import QueueError


logger: logging.Logger = logging.getLogger(name="pool_cue")


class Queue:
    """Class used to interact with the worker(s)/ queue through Redis."""

    redis: ArqRedis

    def __init__(self, settings: QueueSettings) -> None:
        self.settings: QueueSettings = settings
        self.redis: ArqRedis | None = None

    async def connect(self) -> None:
        """Establish a new connection to the Redis queue (if one does not already exist)."""
        if not self.redis:
            self.redis = await create_pool(
                settings_=self.settings.redis_settings,
                job_serializer=self.settings.serializer,
                job_deserializer=self.settings.deserializer,
                default_queue_name=self.settings.queue_name,
            )

    async def disconnect(self) -> None:
        """Close the connection to the Redis queue (if it exists)."""
        if self.redis:
            await self.redis.close(close_connection_pool=True)

    async def _assert_redis_connection(self) -> None:
        if not self.redis:
            raise QueueError("")

    async def get_jobs(self) -> list[JobDef]:
        """Get all jobs that are currently in the queue (queued or running)."""
        await self._assert_redis_connection()
        try:
            jobs: list[JobDef] = await self.redis.queued_jobs(queue_name=self.settings.queue_name)
        except (AssertionError, TimeoutError) as exc:
            logger.warning("", exc_info=exc)
            raise QueueError from exc
        except Exception as exc:
            logger.warning("", exc_info=exc)
            raise QueueError from exc
        else:
            return jobs

    async def _job_already_exists(self, func: str, children: list[str] | None = None) -> bool:
        """
        Check if a job/ task with the given function name already exists in the queue (queued or running).
        If a job spawns child jobs, you can also specify their names to stop new 'parent jobs' from being queued
        as long as any of their children remain in the queue.

        :param func: Name of the job/ task function.
        :param children: An optional list of child job/ task function names.
        :return: A boolean indicating whether the job (and/or its child jobs) already exists in the queue.
        """
        try:
            jobs: list[JobDef] = await self.get_jobs()
        except QueueError as exc:
            logger.warning("Failed to check if job '%s' already exists in the queue!", func, exc_info=exc)
            return True
        if not children:
            return any(job.function == func for job in jobs)
        return any(job.function == func or job.function in children for job in jobs)

    async def push_job(
        self,
        func: str,
        children: list[str] | None = None,
        delay: tuple[int, int] | None = None,
        force: bool = False,
        **kwargs,
    ) -> None:
        """
        Push a new job to the queue.

        By default, the job will not be added to the queue if it (or any of its children) already exists in the queue.
        This behaviour can be controlled with the 'children' and 'force' keyword arguments.

        :param func: Name of the job/ task/ function. Has to match one of the functions registered by the worker.
        :param children: List of child job names created by the function. Used to stop new jobs from being added if any of its children still remain in the queue.
        :param delay: Duration (in seconds) to wait before adding the job to the queue. The duration will be chosen randomly from within the given range.
        :param force: If True, the job will be added to the queue even if it or its children already exist in the queue.
        :param kwargs: Extra keyword arguments that will be passed to the function.
        """
        await self._assert_redis_connection()
        if not force:
            if await self._job_already_exists(func=func, children=children):
                logger.warning("Job '%s' is already queued!", func)
                return
        if delay:
            a, b = delay
            _delay: int = randint(a=a, b=b)
            logger.debug("Adding job '%s' to the queue in %s sec...", func, _delay)
            await sleep(delay=_delay)
        else:
            logger.debug("Adding job '%s' to the queue...", func)
        try:
            await self.redis.enqueue_job(function=func, _job_id=func, _queue_name=self.settings.queue_name, **kwargs)
        except Exception as exc:
            logger.error("Failed to add job '%s' to the queue!", func, exc_info=exc)

    async def __aenter__(self) -> Self:
        await self.connect()
        return self

    async def __aexit__(self, *args, **kwargs) -> None:
        await self.disconnect()
