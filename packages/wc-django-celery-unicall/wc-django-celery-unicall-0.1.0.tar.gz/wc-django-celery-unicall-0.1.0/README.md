# WebCase celery one task caller

Package to call celery tasks only once per unique key.

## Installation

```sh
pip install wc-django-celery-unicall
```

In `settings.py`:

```python
INSTALLED_APPS += [
  'wcd_celery_unicall',
]
```

## Usage

```python
from celery import Celery
from wcd_celery_unicall.task import CACHE_KEY_PREFIX
from wcd_celery_unicall.shortcuts import make_unicall, task

app = Celery('app')

# First after defining and configuring celery app you should change
# the default `Task` class.
# It has a small improvement in `apply_async` method, that will revoke
# other pending tasks that have the same uniqueness key.
app.Task = make_unicall(app.Task)

# ...

from django.core.cache import cache

# All other tasks that you want to check for uniqueness have to be defined
# using a `task` shortcut decorator.
# So instead ow writing `@app.task()` write `@task(app)`.
# But that's not all. To enforce uniqueness check mechanics you must
# provide at least 2 additional parameters: `unicall_key` and `unicall_cache`.
@task(
  # Your celery app:
  app,
  # Function that receives the same arguments that your task, and generates
  # unique key to track task execution.
  unicall_key=lambda user_id, **_: f'sync_user {user_id}',
  # And a django cache backend implementation. This could be anything you
  # wish, but `LockMem` cache backend, for example will be useless.
  # So this should be "global" cache backend, like redis or memcached.
  unicall_cache=cache,
  # Optional. Additional TTL, that will be added to key expirity.
  unicall_additional_ttl=None,
  # Optional. Cache key prefix, if you don't like the default one.
  unicall_key_prefix=CACHE_KEY_PREFIX,
)
def do_something(user_id: int, param2: bool = True, param_3=None):
  pass
```
