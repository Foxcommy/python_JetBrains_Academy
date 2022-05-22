import requests, json
from bs4 import BeautifulSoup

url = input('Input the URL:')


def quote_search(quote_url):
    res = {}
    r = requests.get(quote_url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(r.content, 'html.parser')
    if r and 'title' in url:
        title_m = soup.find('h1').text
        description = soup.find('span', {'data-testid': 'plot-l'}).text
        res['title'] = title_m
        res['description'] = description
        print(res)
    else:
        print('Invalid movie page!')


def save_content(content_url):
    r = requests.get(content_url)
    source_html = open('source.html', 'wb')
    status_code = r.status_code
    if status_code == 200:
        source_html.write(r.content)
        print('Content saved.')
    else:
        print(f'The URL returned {status_code}!')


save_content(url)
