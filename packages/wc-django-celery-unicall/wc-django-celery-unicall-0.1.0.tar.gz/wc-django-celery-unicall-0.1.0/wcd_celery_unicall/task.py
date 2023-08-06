from typing import *
import datetime
from django.core.cache import BaseCache
from functools import wraps
from celery import Celery, Task

from .utils import over_now_timestamp


__all__ = (
    'CACHE_KEY_PREFIX',
    'UnicallTaskMixin', 'UnicallManager',
    'can_proceed', 'unicall_task_quard',
)

CACHE_KEY_PREFIX = 'celery-unicall'

UnicallTaskType = Union[Task, 'UnicallTaskMixin']


class UnicallManager:
    key: Callable
    cache: BaseCache
    # TTL is used to remember task identifier for a bit longer to try to revoke
    # task if wasn't run yet.
    additional_ttl: int = 60

    def __init__(
        self,
        key: Callable,
        cache: BaseCache,
        additional_ttl: Optional[int] = None,
        key_prefix: str = CACHE_KEY_PREFIX,
    ):
        self.key = key
        self.key_prefix = key_prefix
        self.cache = cache
        self.additional_ttl = (
            additional_ttl
            if additional_ttl is not None else
            self.additional_ttl
        )

    def get_key(self, name: str, callback_args, callback_kwargs) -> str:
        # Get the function used to create `self.unicall_key` if the it exists.
        key_generator = (
            self.key.__func__
            if hasattr(self.key, '__func__') else
            self.key
        )

        # Create and return the cache key with the generated unique key suffix.
        return '{prefix}:{task_name}:{unicall_key}'.format(
            prefix=self.key_prefix,
            task_name=name,
            unicall_key=key_generator(
                *(callback_args or ()), **(callback_kwargs or {}),
            )
        )

    def revoke_task(self, app: Celery, cache_key: str):
        task_id = self.cache.get(cache_key)

        if task_id is not None:
            app.AsyncResult(task_id).revoke()
            self.cache.delete(cache_key)

    def get_current_task_id(self, key: str):
        return self.cache.get(key)

    def remember_task(self, cache_key, task_id, ttl):
        self.cache.set(cache_key, task_id, timeout=ttl)

    def make_ttl(self, task_options: dict) -> int:
        ttl_seconds = 0

        if 'eta' in task_options:
            # Get the difference between the ETA and now
            ttl_seconds = over_now_timestamp(task_options['eta'])
        elif 'countdown' in task_options:
            ttl_seconds = task_options['countdown']

        if 'expires' in task_options:
            if isinstance(task_options['expires'], datetime.datetime):
                # Get the difference between the countdown and now
                seconds_until_expiry = over_now_timestamp(
                    task_options['expires'])
            else:
                seconds_until_expiry = task_options['expires']

            if seconds_until_expiry < ttl_seconds:
                ttl_seconds = seconds_until_expiry

        return max(ttl_seconds, 0) + self.additional_ttl


class UnicallTaskMixin:
    abstract = True

    unicall_manager: Optional[UnicallManager] = None

    def apply_async(
        self,
        args=None, kwargs=None,
        task_id=None, producer=None,
        link=None, link_error=None,
        **options,
    ):
        manager = self.unicall_manager
        has_manager = manager is not None

        if has_manager:
            # Revoke any task with the same uniqueness key.
            unique_cache_key = manager.get_key(self.name, args, kwargs)
            manager.revoke_task(self.app, unique_cache_key)

        # Run task
        rv = super().apply_async(
            args, kwargs, task_id, producer, link, link_error, **options
        )

        if has_manager:
            # Remember current task id to be able to revoke it
            manager.remember_task(
                unique_cache_key, rv.task_id, manager.make_ttl(options),
            )

        return rv


def can_proceed(task: UnicallTaskType, args, kwargs) -> bool:
    manager: Optional[UnicallManager] = task.unicall_manager

    if manager is None:
        return True

    key = manager.get_key(task.name, args, kwargs)
    task_id = manager.get_current_task_id(key)

    return task_id == task.request.id


def unicall_task_quard(task_fn: Callable):
    def wrapper(task: UnicallTaskType, *args, **kwargs):
        if not can_proceed(task, args, kwargs):
            return

        return task_fn(task, *args, **kwargs)

    return wraps(task_fn)(wrapper)
