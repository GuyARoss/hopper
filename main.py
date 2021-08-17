import os
import sys
import pathlib

from local_player import LocalPlayer

from reddit_search import RedditSearch
from downloader import download_videos

PATH = pathlib.Path(__file__).parent.absolute()

def keyword_downloader(query: str):
    s = RedditSearch(query=query)
    resp = s.fetch_from_page(10)

    download_videos(
        list(map(lambda x: x['uri'], resp)),
        f'{PATH}/temp',
    )


def player():
    dirs = os.listdir(f'{PATH}/temp')
    player = LocalPlayer()
    
    for dir in dirs:
        player.play_video(f'{PATH}/temp/{dir}')


if __name__ == '__main__':
    keyword_downloader(sys.argv[1])

    while True:
        player()