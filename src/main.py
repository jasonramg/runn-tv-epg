from lxml import etree

from src.downloader import Downloader


def main():
    xml = Downloader().download()

    root = etree.fromstring(xml)

    print(f"Channels: {len(root.findall('item'))}")

    first = root.find("item")

    print("\n=== FIRST CHANNEL ===")
    print("Title:", first.findtext("title"))
    print("Code :", first.findtext("channelCode"))
    print("ID   :", first.findtext("id"))

    schedules = first.find("schedules")

    print("Schedules:", len(schedules.findall("schedules")))

    program = schedules.find("schedules")

    print("\n=== FIRST PROGRAM ===")
    print("Name      :", program.findtext("programName"))
    print("Start     :", program.findtext("startTimeEpoch"))
    print("Duration  :", program.findtext("durationSeconds"))
    print("Language  :", program.findtext("language"))
    print("Age Rating:", program.findtext("ageRating"))


if __name__ == "__main__":
    main()