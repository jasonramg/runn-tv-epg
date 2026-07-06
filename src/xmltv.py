from pathlib import Path
import os
from lxml import etree

from .config import OUTPUT_XML


def dt(dt):
    return dt.strftime("%Y%m%d%H%M%S +0000")


def write_xmltv(channels, programmes):

    tv = etree.Element(
        "tv",
        generator_info_name="RunnTV XMLTV Generator",
        source_info_name="RunnTV"
    )

    # Channels
    for ch in channels:

        c = etree.SubElement(
            tv,
            "channel",
            id=ch.id
        )

        etree.SubElement(
            c,
            "display-name"
        ).text = ch.name

        if ch.logo:
            etree.SubElement(
                c,
                "icon",
                src=ch.logo
            )

    # Programmes
    for p in programmes:

        prog = etree.SubElement(
            tv,
            "programme",
            channel=p.channel,
            start=dt(p.start),
            stop=dt(p.stop)
        )

        etree.SubElement(
            prog,
            "title",
            lang="en"
        ).text = p.title

        if p.desc:
            etree.SubElement(
                prog,
                "desc",
                lang="en"
            ).text = p.desc

        if p.language:
            etree.SubElement(
                prog,
                "language"
            ).text = p.language

        if p.rating:

            rating = etree.SubElement(
                prog,
                "rating"
            )

            etree.SubElement(
                rating,
                "value"
            ).text = p.rating

        if p.icon:

            etree.SubElement(
                prog,
                "icon",
                src=p.icon
            )

    OUTPUT_XML.parent.mkdir(exist_ok=True)

    tmp = Path(str(OUTPUT_XML) + ".tmp")

    etree.ElementTree(tv).write(
        tmp,
        encoding="UTF-8",
        xml_declaration=True,
        pretty_print=True
    )

    os.replace(tmp, OUTPUT_XML)