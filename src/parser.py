from datetime import datetime, timedelta, timezone
from lxml import etree
from .models import Channel, Programme


def parse(xml: bytes):
    root = etree.fromstring(xml)

    channels = []
    programmes = []

    for item in root.findall("item"):

        channel_id = item.findtext("channelCode", "")
        channel_name = item.findtext("title", "")

        base = item.findtext("baseSourceLocation", "")

        logo = ""
        logo_node = item.find("./images/logo/web")
        if logo_node is not None and logo_node.text:
            logo = base + logo_node.text

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

            icon = ""
            icon_node = sched.find("./infoImages/web")
            if icon_node is not None and icon_node.text:
                icon = base + icon_node.text

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