from pytubefix import YouTube
from pytubefix.cli import on_progress

URLS: dict[str, str] = {
    "koko": "https://www.youtube.com/watch?v=FqJf1mB5PjQ",
    "alex": "https://www.youtube.com/watch?v=ldYkFdu5FJk",
    "silbo-gomero": "https://www.youtube.com/watch?v=C0CIRCjoICA",
    "kus-dili": "https://www.youtube.com/watch?v=l117wfB0g3o",
    "protactile": "https://www.youtube.com/watch?v=8im72wFTa9Y",
    "womb": "https://www.youtube.com/watch?v=yWBgy55EkIM",
    "sucking": "https://www.youtube.com/watch?v=psgv41HVdaE",
    "hpp": "https://www.youtube.com/watch?v=WvM5bqUsbu8",
}


def download_video(url: str, file: str):

    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    ys = yt.streams.get_highest_resolution()
    if ys and file:
        fn = file + ".mp4"
        ys.download("img", filename=fn)


if __name__ == "__main__":
    for fn, url in URLS.items():
        download_video(url, fn)
