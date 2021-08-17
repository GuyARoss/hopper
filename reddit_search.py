import time
import requests

from bs4 import BeautifulSoup

def format_posts_page(soup):
    posts = []

    for domain in soup.find_all('div', class_='search-result-link'):
        title = domain.find('a', class_='search-title')

        post = {
            'title': title.text.lower() if title else 'n/ a',
            'uri': domain.find('a', class_='search-title')['href'],
        }
        
        posts.append(post)

    return posts

headers = {'User-Agent': 'Mozilla/5.0'}

class RedditSearch():
    def __init__(self, query: str, sort: str = 'new', include_over_18 = True):
        self.url = f'https://old.reddit.com/search/?q={query}&sort={sort}&t=all'
        if include_over_18:
            self.url += "&restrict_sr=&include_over_18=on"

        self.page = requests.get(
            self.url,
            headers=headers,
        )
        self.soup = BeautifulSoup(self.page.text, 'html.parser')

    def fetch_from_page(self, page_count):
        local_soup = self.soup
        page = self.page

        page_data = []

        for _ in range(page_count):
            page_data += (format_posts_page(local_soup))
            time.sleep(2) 

            next_button = local_soup.find("footer", class_="nextprev")
            if next_button == None:
                break
        
            next_page_link = next_button.find("a").attrs['href']
            page = requests.get(next_page_link, headers=headers)
            local_soup = BeautifulSoup(page.text, 'html.parser')


        return page_data