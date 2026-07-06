import hashlib
import subprocess
import sys
from pathlib import Path

from src.main import main

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


print("Generating EPG...")
main()

new_hash = sha256(XML)

old_hash = ""

if HASH.exists():
    old_hash = HASH.read_text().strip()

if new_hash == old_hash:
    print("No changes detected.")
    sys.exit(0)

HASH.write_text(new_hash)

print("Changes detected.")

subprocess.run(["git", "add", "output"], check=True)

result = subprocess.run(
    ["git", "diff", "--cached", "--quiet"]
)

if result.returncode == 0:
    print("Nothing changed.")
    sys.exit(0)

subprocess.run(
    ["git", "commit", "-m", "Automatic EPG update"],
    check=True
)

subprocess.run(["git", "push"], check=True)

print("GitHub updated.")