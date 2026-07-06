import gzip
import shutil

from .config import OUTPUT_XML, OUTPUT_GZ


def compress():
    with open(OUTPUT_XML, "rb") as src:
        with gzip.open(OUTPUT_GZ, "wb", compresslevel=9) as dst:
            shutil.copyfileobj(src, dst)