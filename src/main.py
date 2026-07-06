from .downloader import Downloader


def main():

    xml = Downloader().download()

    print(f"Downloaded {len(xml)} bytes")


if __name__ == "__main__":
    main()