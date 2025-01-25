# Torrent and Video Downloader with aria2c and yt-dlp

This script allows you to download videos using `aria2c` for torrent files and `yt-dlp` for video URLs (e.g., YouTube or other supported platforms). The user can select the quality of the video when using `yt-dlp`.

## Requirements

Before running the script, make sure you have the following software installed:

1. **aria2c** - A fast and feature-rich download utility for torrents.
2. **yt-dlp** - A command-line tool for downloading videos from YouTube and other websites.

### Install aria2c
Follow the instructions to install **aria2c** on your system:

- **Windows:** Download from [aria2 releases on GitHub](https://github.com/aria2/aria2/releases).
- **Linux:** Use `sudo apt install aria2` (Debian/Ubuntu-based) or check your distribution's package manager.
- **macOS:** Use `brew install aria2` (Homebrew).

Ensure that `aria2c` is added to your system's PATH.

### Install yt-dlp
To install `yt-dlp`, use pip:

```bash
pip install yt-dlp
