from pathlib import Path
from lxml import etree


def validate_xml(path: Path):

    etree.parse(path)

    return True