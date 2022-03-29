import typer
from ytdownloader import download_music, download_video

app = typer.Typer()

@app.command()
def song(song: str):
    download_music(song)

@app.command()
def video(video: str):
    download_video(video)

if __name__ == '__main__':
    app()