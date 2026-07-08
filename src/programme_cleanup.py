from datetime import timedelta

from .config import KEEP_HISTORY_DAYS


def keep_recent_programmes(programmes):

    if not programmes:
        return programmes

    latest = max(
        p.stop
        for p in programmes
    )

    cutoff = latest - timedelta(
        days=KEEP_HISTORY_DAYS
    )

    return [
        p
        for p in programmes
        if p.stop >= cutoff
    ]