#!/usr/bin/python3
import subprocess
from pathlib import Path

def yt_to_ogg(url, output_path="PATH"):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    Path(output_path).mkdir(parents=True, exist_ok=True)

    subprocess.run([
        "yt-dlp",
        "-x",
        "--audio-format", "vorbis",
        "--force-ipv4",
        "-o", f"{output_path}/%(title)s.%(ext)s",
        url
    ], check=True)

if __name__ == "__main__":
    youtube_url = input("Enter YouTube video URL: ").strip()
    yt_to_ogg(youtube_url)
