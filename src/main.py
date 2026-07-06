from src.downloader import Downloader
from src.parser import parse
from src.xmltv import write_xmltv
from src.compressor import compress
from src.stats import write_stats
from src.m3u import write_playlist
from src.channels_json import write_channels
from src.manifest import write_manifest
from src.logger import log

def main():

    xml = Downloader().download()

    channels, programmes = parse(xml)

    log.info("Channels   : %d", len(channels))
    log.info("Programmes : %d", len(programmes))

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

    print()

    log.info("XMLTV written.")
    log.info("Playlist written.")
    log.info("channels.json written.")
    log.info("stats.json written.")
    log.info("manifest.json written.")
    log.info("Build completed successfully.")


if __name__ == "__main__":
    main()