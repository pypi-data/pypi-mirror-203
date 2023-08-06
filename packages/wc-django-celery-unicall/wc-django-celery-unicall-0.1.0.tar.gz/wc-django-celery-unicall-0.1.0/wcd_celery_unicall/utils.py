from typing import *
from datetime import datetime
from django.utils import timezone


__all__ = 'now', 'over_now_timestamp',


def now(against_date: Optional[datetime] = None) -> datetime:
    if against_date is not None:
        return datetime.now(tz=against_date.tzinfo)

    return timezone.now()


def over_now_timestamp(date: datetime) -> int:
    return int((date - now(date)).total_seconds())
