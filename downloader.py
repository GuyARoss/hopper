from typing import List

from redvid import Downloader


def download_videos(URLs: List[str], to_path: str):
    for idx in range(len(URLs)):
        try:
            dwn = Downloader(
                url=URLs[idx],
                max_q=True,
                path=to_path
            )

            dwn.max = True
            dwn.max_d = 120

            dwn.download()
        except:
            print(f'cannot dowload {URLs[idx]}')
            continue
