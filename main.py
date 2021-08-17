import os
import sys
import pathlib
import time

from local_player import LocalPlayer

from reddit_search import RedditSearch
from downloader import download_videos

PATH = pathlib.Path(__file__).parent.absolute()

def keyword_downloader(query: str):
    s = RedditSearch(query=query)
    resp = s.fetch_from_page(10)

    download_videos(
        list(map(lambda x: x['uri'], resp)),
        f'{PATH}/temp/{query}',
    )


def play(query:str, player: LocalPlayer):
    dirs = os.listdir(f'{PATH}/temp/{query}')

    while len(dirs) <= 1:
        dirs = os.listdir(f'{PATH}/temp/{query}')
        time.sleep(5)


    for dir in dirs:
        player.play_video(f'{PATH}/temp/{query}/{dir}')


if __name__ == '__main__':
    type = sys.argv[1]
    query = sys.argv[2]
    
    if not os.path.exists(f'{PATH}/temp/{query}'):
        os.mkdir(f'{PATH}/temp/{query}')

    if type == 'dwn':    
        keyword_downloader(query)

    if type == 'ply':
        player = LocalPlayer()
        while True:
            play(query, player)