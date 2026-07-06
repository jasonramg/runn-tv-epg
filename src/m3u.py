from pathlib import Path
from .categories import get_category

OUTPUT = Path("output/playlist.m3u")


def write_playlist(channels):

    OUTPUT.parent.mkdir(exist_ok=True)

    with open(OUTPUT, "w", encoding="utf-8") as f:

        f.write("#EXTM3U\n")

        for ch in channels:

            line = (
                '#EXTINF:-1 '
                f'tvg-id="{ch.id}" '
                f'tvg-name="{ch.name}" '
                f'tvg-logo="{ch.logo}" '
                f'group-title="{get_category(ch.id)}",'
                f'{ch.name}'
            )

            f.write(line + "\n")

            f.write(ch.play_url + "\n\n")