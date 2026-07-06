from src.downloader import Downloader
from src.parser import parse


def main():
    xml = Downloader().download()

    channels, programmes = parse(xml)

    print(f"Channels   : {len(channels)}")
    print(f"Programmes : {len(programmes)}")

    if programmes:
        p = programmes[0]

        print()
        print("First programme")
        print("----------------")
        print("Channel :", p.channel)
        print("Title   :", p.title)
        print("Start   :", p.start)
        print("Stop    :", p.stop)
        print("Rating  :", p.rating)


if __name__ == "__main__":
    main()