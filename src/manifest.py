import json
from datetime import datetime, timezone
from pathlib import Path

OUTPUT = Path("output/manifest.json")


def write_manifest(channels, programmes):

    manifest = {
        "generator": "RunnTV Toolkit",
        "version": "1.1.0",
        "generated": datetime.now(timezone.utc).isoformat(),

        "channels": len(channels),
        "programmes": len(programmes),

        "downloads": {
            "epg": "epg.xml",
            "epg_gz": "epg.xml.gz",
            "playlist": "playlist.m3u",
            "channels": "channels.json",
            "stats": "stats.json"
        }
    }

    OUTPUT.write_text(
        json.dumps(
            manifest,
            indent=4
        ),
        encoding="utf8"
    )