from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET

from .models import Channel, Programme


def read_xmltv(path: Path):

    if not path.exists():
        return [], []

    tree = ET.parse(path)
    root = tree.getroot()

    channels = []

    for c in root.findall("channel"):

        icon = ""

        icon_tag = c.find("icon")
        if icon_tag is not None:
            icon = icon_tag.attrib.get("src", "")

        channels.append(
            Channel(
                id=c.attrib["id"],
                name=c.findtext("display-name", ""),
                logo=icon,
                play_url=""
            )
        )

    programmes = []

    for p in root.findall("programme"):

        icon = ""
        icon_tag = p.find("icon")
        if icon_tag is not None:
            icon = icon_tag.attrib.get("src", "")

        rating = ""
        rating_tag = p.find("rating/value")
        if rating_tag is not None:
            rating = rating_tag.text or ""

        language = p.findtext("language", "")

        programmes.append(
            Programme(
                channel=p.attrib["channel"],
                title=p.findtext("title", ""),
                desc=p.findtext("desc", ""),
                language=language,
                rating=rating,
                start=datetime.strptime(
                    p.attrib["start"],
                    "%Y%m%d%H%M%S %z"
                ),
                stop=datetime.strptime(
                    p.attrib["stop"],
                    "%Y%m%d%H%M%S %z"
                ),
                icon=icon
            )
        )

    return channels, programmes