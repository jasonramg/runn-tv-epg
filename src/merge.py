from datetime import datetime, timezone
from src.logger import log


def merge_programmes(old_programmes,
                     new_programmes):

    updated_channels = {
        p.channel
        for p in new_programmes
    }

    merged = []

    for p in old_programmes:

        if p.channel not in updated_channels:
            merged.append(p)

    merged.extend(new_programmes)

    now = datetime.now(timezone.utc)

    merged = [
        p
        for p in merged
        if p.stop > now
    ]

    merged.sort(
        key=lambda p: (
            p.channel,
            p.start
        )
    )

    log.info(
        "Merged result: %d programmes",
        len(merged)
    )

    return merged