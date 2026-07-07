from src.logger import log


def merge_channels(old_channels, new_channels):

    merged = {}

    # Keep existing channels
    for channel in old_channels:
        merged[channel.id] = channel

    # Replace with newer channels
    for channel in new_channels:
        merged[channel.id] = channel

    result = sorted(
        merged.values(),
        key=lambda c: c.name.lower()
    )

    log.info(
        "Merged channels: %d",
        len(result)
    )

    return result