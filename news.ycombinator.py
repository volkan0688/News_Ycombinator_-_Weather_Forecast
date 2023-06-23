import requests
from bs4 import BeautifulSoup

target_url = "https://news.ycombinator.com/"
found_links = []


def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def capture_url(url):
    news_url = make_request(target_url)
    id_number = 1
    for title_news in news_url.find_all('span', {'class': 'titleline'}):
        found_title_news = title_news.getText()
        print(f"{id_number} - {found_title_news}")
        id_number += 1


capture_url(target_url)
