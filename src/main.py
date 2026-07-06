from src.downloader import Downloader
from src.parser import parse
from src.xmltv import write_xmltv


def main():

    xml = Downloader().download()

    channels, programmes = parse(xml)

    print(f"Channels   : {len(channels)}")
    print(f"Programmes : {len(programmes)}")

    write_xmltv(
        channels,
        programmes
    )

    print()
    print("EPG generated successfully.")

    print("\nChannels returned by API:")
    for ch in channels:
        print(ch.id, "-", ch.name)


if __name__ == "__main__":
    main()