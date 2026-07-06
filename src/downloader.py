from __future__ import annotations

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .config import API_URL, TIMEOUT, USER_AGENT
from .logger import log


class Downloader:

    def __init__(self):
        self.session = requests.Session()

        retry = Retry(
            total=5,
            connect=5,
            read=5,
            backoff_factor=1,
            status_forcelist=[
                429,
                500,
                502,
                503,
                504
            ],
            allowed_methods=["GET"]
        )

        adapter = HTTPAdapter(max_retries=retry)

        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        self.session.headers.update({
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-IN,en;q=0.5",
            "Upgrade-Insecure-Requests": "1",
        })

    def download(self) -> bytes:

        log.info("Downloading EPG...")

        r = self.session.get(
            API_URL,
            timeout=TIMEOUT
        )

        print("Final URL:", r.url)
        print("Content-Type:", r.headers.get("Content-Type"))
        print("Content-Length:", r.headers.get("Content-Length"))

        # Add these lines
        print("Server:", r.headers.get("Server"))
        print("Via:", r.headers.get("Via"))
        print("CF-Cache-Status:", r.headers.get("CF-Cache-Status"))
        print("Age:", r.headers.get("Age"))
        print("ETag:", r.headers.get("ETag"))
        print("Last-Modified:", r.headers.get("Last-Modified"))

        log.info("Status: %s", r.status_code)

        r.raise_for_status()

        content = r.content

        if len(content) == 0:
            raise RuntimeError("Server returned empty response.")

        # Detect HTML
        if content.lstrip().startswith(b"<!DOCTYPE html") or \
           content.lstrip().startswith(b"<html"):

            with open("response.html", "wb") as f:
                f.write(content)

            raise RuntimeError(
                "Server returned HTML instead of XML. "
                "Saved as response.html"
            )

        # Detect JSON
        if content.lstrip().startswith(b"{") or \
           content.lstrip().startswith(b"["):

            with open("response.json", "wb") as f:
                f.write(content)

            raise RuntimeError(
                "Server returned JSON instead of XML. "
                "Saved as response.json"
            )

        log.info("First 200 bytes of response:")

        print(repr(content[:200]))

        with open("response.bin", "wb") as f:
            f.write(content)

        log.info(
            "Downloaded %.2f MB",
            len(content) / 1024 / 1024
        )

        return content