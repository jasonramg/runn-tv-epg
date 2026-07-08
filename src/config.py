from pathlib import Path

API_URL = "https://prod-epg.runn.tv/runtv/v1/schedule/getChannelEpg"

OUTPUT_DIR = Path("output")

OUTPUT_XML = OUTPUT_DIR / "epg.xml"

OUTPUT_GZ = OUTPUT_DIR / "epg.xml.gz"

TIMEOUT = 60

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
)

DEBUG = False

KEEP_HISTORY_DAYS = 3

IMAGE_PREFERENCE = (
    "web",
    "mobile",
    "tv",
    "partner",
)