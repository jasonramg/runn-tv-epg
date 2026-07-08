from datetime import datetime, timedelta, timezone

from .config import KEEP_HISTORY_DAYS


def keep_recent_programmes(programmes):

    cutoff = (
        datetime.now(timezone.utc)
        - timedelta(days=KEEP_HISTORY_DAYS)
    )

    return [
        p
        for p in programmes
        if p.stop >= cutoff
    ]