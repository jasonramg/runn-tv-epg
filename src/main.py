from pathlib import Path

from src.downloader import Downloader
from src.parser import parse
from src.xmltv import write_xmltv
from src.compressor import compress
from src.stats import write_stats
from src.m3u import write_playlist
from src.channels_json import write_channels
from src.manifest import write_manifest
from src.logger import log

from src.merge import merge_programmes
from src.xmltv_reader import read_xmltv
from src.merge_channels import merge_channels
from src.channels_reader import read_channels
from src.channel_state import analyze_channels
from src.programme_cleanup import keep_recent_programmes

OUTPUT_XML = Path("output/epg.xml")

def main():

    xml = Downloader().download()

    channels, programmes = parse(xml)

    downloaded_channel_count = len(channels)
    downloaded_programme_count = len(programmes)

    if OUTPUT_XML.exists():

        old_channels = read_channels(
            Path("output/channels.json")
        )

        _, old_programmes = read_xmltv(
            OUTPUT_XML
        )

        new_ids = {
            c.id
            for c in channels
        }

        old_ids = {
            c.id
            for c in old_channels
        }

        state = analyze_channels(
            old_ids,
            new_ids
        )

        if state.is_partial:

            log.info(
                "Partial EPG detected (%d/%d channels).",
                len(new_ids),
                len(old_ids)
            )

            channels = merge_channels(
                old_channels,
                channels
            )

            programmes = merge_programmes(
                old_programmes,
                programmes
            )

        elif state.has_new_channels:

            log.info(
                "Channel lineup changed."
            )

            log.info(
                "Added channels: %d",
                len(state.added)
            )

            log.info(
                "Missing channels: %d",
                len(state.missing)
            )

        else:

            log.info(
                "Complete channel lineup."
            )

    before = len(programmes)

    programmes = keep_recent_programmes(
        programmes
    )

    removed = before - len(programmes)

    log.info(
        "Removed %d expired programmes",
        removed
    )
    log.info("Downloaded channels : %d", downloaded_channel_count)
    log.info("Downloaded programmes : %d", downloaded_programme_count)

    log.info("Final channels      : %d", len(channels))
    log.info("Final programmes    : %d", len(programmes))

    write_xmltv(
        channels,
        programmes
    )

    write_playlist(channels)

    write_channels(channels)

    compress()

    write_stats(
        channels,
        programmes
    )

    write_manifest(channels, programmes)

    from src.publisher import publish
    publish()

    print()

    log.info("XMLTV written.")
    log.info("Playlist written.")
    log.info("channels.json written.")
    log.info("stats.json written.")
    log.info("manifest.json written.")
    log.info("Build completed successfully.")

    return {
        "downloaded_channels": downloaded_channel_count,
        "downloaded_programmes": downloaded_programme_count,
        "final_channels": len(channels),
        "final_programmes": len(programmes),
    }


if __name__ == "__main__":
    main()