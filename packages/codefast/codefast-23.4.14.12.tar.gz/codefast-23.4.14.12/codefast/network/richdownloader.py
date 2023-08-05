"""
A rudimentary URL downloader (like wget or curl) to demonstrate Rich progress bars.
"""
import requests
import os.path
import sys
from concurrent.futures import ThreadPoolExecutor
import signal
from functools import partial
from threading import Event
from typing import Iterable
from urllib.request import urlopen

from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)

progress = Progress(
    TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    DownloadColumn(),
    "•",
    TransferSpeedColumn(),
    "•",
    TimeRemainingColumn(),
)

done_event = Event()


def handle_sigint(signum, frame):
    done_event.set()


signal.signal(signal.SIGINT, handle_sigint)


def copy_url(task_id: TaskID, url: str, path: str) -> None:
    """Copy data from a url to a local file."""
    progress.console.log(f"Requesting {url}")
    part = os.path.getsize(path) if os.path.exists(path) else 0
    response = requests.get(url,
                            stream=True,
                            headers={'Range': 'bytes=%d-' % part})
    # This will break if the response doesn't contain content length
    total = int(response.headers["content-length"])
    if total > (1 << 3):
        progress.update(task_id, total=total)

        with open(path, "ab") as dest_file:
            progress.start_task(task_id)
            for data in response.iter_content(1024):
                dest_file.write(data)
                progress.update(task_id, advance=len(data))
                if done_event.is_set():
                    return
    progress.console.log(f"Downloaded {path}")


def download(urls: Iterable[str], dest_dir: str):
    """Download multiple files to the given directory."""
    if isinstance(urls, str):
        urls = [urls]

    with progress:
        with ThreadPoolExecutor(max_workers=4) as pool:
            for url in urls:
                filename = url.split("/")[-1]
                dest_path = os.path.join(dest_dir, filename) if dest_dir else filename
                task_id = progress.add_task("download",
                                            filename=filename,
                                            start=False)
                pool.submit(copy_url, task_id, url, dest_path)


if __name__ == "__main__":
    # Try with https://releases.ubuntu.com/20.04/ubuntu-20.04.3-desktop-amd64.iso
    if sys.argv[1:]:
        download(sys.argv[1:], "./")
    else:
        print("Usage:\n\tpython downloader.py URL1 URL2 URL3 (etc)")
