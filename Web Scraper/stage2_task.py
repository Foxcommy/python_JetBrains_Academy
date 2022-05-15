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


quote_search(url)
