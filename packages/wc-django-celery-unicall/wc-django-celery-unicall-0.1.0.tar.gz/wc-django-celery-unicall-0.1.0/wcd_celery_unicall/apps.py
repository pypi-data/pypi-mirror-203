from django.apps import AppConfig
from django.utils.translation import pgettext_lazy


__all__ = 'CeleryUnicallConfig',


class CeleryUnicallConfig(AppConfig):
    name = 'wcd_celery_unicall'
    verbose_name = pgettext_lazy('wcd_celery_unicall', 'Celery unicall')
