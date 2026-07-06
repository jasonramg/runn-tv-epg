import json
from pathlib import Path

from .categories import get_category

OUTPUT = Path("output/channels.json")


def write_channels(channels):

    OUTPUT.parent.mkdir(exist_ok=True)

    data = []

    for ch in channels:

        data.append(
            {
                "id": ch.id,
                "name": ch.name,
                "category": get_category(ch.id),
                "logo": ch.logo,
                "stream": ch.play_url
            }
        )

    OUTPUT.write_text(
        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf8"
    )