from typing import *
from celery import Task
from functools import wraps
from django.core.cache import BaseCache

from .task import (
    UnicallTaskMixin, unicall_task_quard, UnicallManager, CACHE_KEY_PREFIX
)


__all__ = 'make_unicall', 'task',

T = TypeVar('T')


def make_unicall(task_cls: Task = Task):
    """Creates a new, abstract Celery Task class that enables tasks to run
    once per time.

    Returns:
        The new Celery task base class with unique task-handling
        functionality mixed in.
    """
    return type(str('UnicallTask'), (UnicallTaskMixin, task_cls), {})


def task(
    app,
    *_,
    unicall_key: Optional[Callable] = None,
    unicall_cache: Optional[BaseCache] = None,
    unicall_additional_ttl: Optional[int] = None,
    unicall_key_prefix: str = CACHE_KEY_PREFIX,
    **options
):
    bindable = options.get('bind', False)
    options['bind'] = True

    options['unicall_manager'] = (
        None if unicall_cache is None or unicall_key is None else
        UnicallManager(
            unicall_key, cache=unicall_cache,
            additional_ttl=unicall_additional_ttl,
            key_prefix=unicall_key_prefix,
        )
    )

    def wrapper(fn: T) -> T:
        task_fn = fn if bindable else lambda _, *a, **kw: fn(*a, **kw)

        return app.task(**options)(wraps(fn)(unicall_task_quard(task_fn)))

    return wrapper
