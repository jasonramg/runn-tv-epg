import hashlib
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timezone

from src.main import main
from src.version import VERSION
from src.gitutils import git
from src.logger import log

git("fetch", "origin")

log.info("RunnTV Toolkit v%s", VERSION)

XML = Path("output/epg.xml")
HASH = Path("output/.epg.sha256")


def sha256(path):
    h = hashlib.sha256()

    with open(path, "rb") as f:
        while True:
            data = f.read(1024 * 1024)
            if not data:
                break
            h.update(data)

    return h.hexdigest()


log.info("Generating EPG...")

try:
    result = main()

    is_full_update = (
        result["downloaded_channels"] >=
        result["final_channels"]
    )

except KeyboardInterrupt:
    print("\nBuild cancelled by user.")
    sys.exit(1)

except Exception as e:
    log.exception("Build failed")
    sys.exit(1)

new_hash = sha256(XML)

old_hash = ""

if HASH.exists():
    old_hash = HASH.read_text().strip()

if new_hash == old_hash:
    print("No changes detected.")
    sys.exit(0)

HASH.write_text(new_hash)

log.info("Changes detected.")

git("add", "output", "docs/output")

result = subprocess.run(
    ["git", "diff", "--cached", "--quiet"]
)

if result.returncode == 0:
    print("Nothing changed.")
    sys.exit(0)

timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

message = f"EPG Update - {timestamp}"

git("commit", "-m", message)

try:
    git("push")
    log.info("GitHub updated.")

except Exception:

    if not is_full_update:

        log.warning(
            "Push rejected after partial update. "
            "Skipping."
        )
        sys.exit(0)

    log.warning(
        "Push rejected after full update. "
        "Please rerun update.py."
    )
    sys.exit(1)