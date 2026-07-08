from datetime import datetime, timedelta, timezone
from lxml import etree
from .models import Channel, Programme
from .config import IMAGE_PREFERENCE

def find_best_image(parent):

    if parent is None:
        return ""

    for tag in IMAGE_PREFERENCE:

        node = parent.find(tag)

        if node is not None and node.text:
            return node.text

    # Fallback: first non-empty child
    for node in parent:

        if node.text:
            return node.text

    return ""


def parse(xml: bytes):
    root = etree.fromstring(xml)

    channels = []
    programmes = []

    for item in root.findall("item"):

        channel_id = item.findtext("channelCode", "")
        channel_name = item.findtext("title", "")

        base = item.findtext("baseSourceLocation", "")

        logo = find_best_image(
            item.find("./images/logo")
        )

        if logo:
            logo = base + logo

        channels.append(
            Channel(
                id=channel_id,
                name=channel_name,
                logo=logo,
                play_url=item.findtext("playUrl", "")
            )
        )

        schedules = item.find("schedules")
        if schedules is None:
            continue

        for sched in schedules.findall("schedules"):

            start_ms = int(sched.findtext("startTimeEpoch", "0"))
            duration = int(sched.findtext("durationSeconds", "0"))

            start = datetime.fromtimestamp(
                start_ms / 1000,
                tz=timezone.utc,
            )

            stop = start + timedelta(seconds=duration)

            icon = find_best_image(
                sched.find("./infoImages")
            )

            if icon:
                icon = base + icon

            programmes.append(
                Programme(
                    channel=channel_id,
                    title=sched.findtext("programName", ""),
                    desc=sched.findtext("description", ""),
                    language=sched.findtext("language", ""),
                    rating=sched.findtext("ageRating", ""),
                    start=start,
                    stop=stop,
                    icon=icon,
                )
            )

    return channels, programmes