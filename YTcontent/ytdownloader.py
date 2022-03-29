from __future__ import unicode_literals
from yt_dlp import YoutubeDL

def download_music(song: str, quality: int = 256):
    # low quality: 48 kbps medium quality: 128kbps high quality: 256 kbps
    ydl_opts = {'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': str(quality)}]}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([song])

def download_video(video: str):
    ydl_opts = {
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }]
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video])