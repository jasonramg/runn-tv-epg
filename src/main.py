from lxml import etree

from src.downloader import Downloader


def main():
    xml = Downloader().download()

    print(f"Downloaded {len(xml)} bytes")

    root = etree.fromstring(xml)

    print(f"Root tag: {root.tag}")

    items = root.findall("item")

    print(f"Channels found: {len(items)}")


if __name__ == "__main__":
    main()