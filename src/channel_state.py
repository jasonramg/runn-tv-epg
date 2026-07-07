from dataclasses import dataclass


@dataclass(slots=True)
class ChannelState:
    is_partial: bool
    is_complete: bool
    has_new_channels: bool
    added: set[str]
    missing: set[str]


def analyze_channels(old_ids, new_ids):

    added = new_ids - old_ids
    missing = old_ids - new_ids

    is_partial = (
        len(new_ids) < len(old_ids)
        and new_ids.issubset(old_ids)
    )

    is_complete = (
        len(added) == 0
        and len(missing) == 0
    )

    has_new_channels = len(added) > 0

    return ChannelState(
        is_partial,
        is_complete,
        has_new_channels,
        added,
        missing
    )