import os
import pathlib

from reddit_search import RedditSearch
from downloader import download_videos
from player import LocalPlayer

PATH = pathlib.Path(__file__).parent.absolute()

def keyword_downloader():
    s = RedditSearch(query='kabul')
    resp = s.fetch_from_page(5)

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
    player()