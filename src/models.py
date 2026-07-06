from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Channel:
    id: str
    name: str
    logo: str
    play_url: str


@dataclass(slots=True)
class Programme:
    channel: str
    title: str
    desc: str
    language: str
    rating: str
    start: datetime
    stop: datetime
    icon: str