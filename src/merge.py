from src.logger import log


def merge_programmes(old_programmes, new_programmes):

    merged = {}

    # Add old programmes first
    for p in old_programmes:

        key = (
            p.channel,
            p.start
        )

        merged[key] = p

    # Replace with newer downloaded versions
    for p in new_programmes:

        key = (
            p.channel,
            p.start
        )

        merged[key] = p

    programmes = sorted(
        merged.values(),
        key=lambda p: (
            p.channel,
            p.start
        )
    )

    log.info(
        "Merged result: %d programmes",
        len(programmes)
    )

    return programmes