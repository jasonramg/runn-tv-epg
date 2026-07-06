import json
from datetime import datetime
from pathlib import Path

STATS = Path("output/stats.json")


def write_stats(channels, programmes):

    data = {
        "generated": datetime.utcnow().isoformat() + "Z",
        "channels": len(channels),
        "programmes": len(programmes)
    }

    STATS.write_text(
        json.dumps(
            data,
            indent=4
        ),
        encoding="utf8"
    )