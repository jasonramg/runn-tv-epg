import json
from pathlib import Path

from .models import Channel


def read_channels(path: Path):

    if not path.exists():
        return []

    data = json.loads(path.read_text(encoding="utf-8"))

    channels = []

    for ch in data:
        channels.append(
            Channel(
                id=ch["id"],
                name=ch["name"],
                logo=ch["logo"],
                play_url=ch["stream"],
            )
        )

    return channels