import requests, string
from bs4 import BeautifulSoup

url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
base_url = 'https://www.nature.com'
r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
soup = BeautifulSoup(r.content, 'html.parser')
nature_news = []
all_articles = soup.find_all('li', 'app-article-list-row__item')


def generate_filename(article_name):
    article_name_beauty = ''
    for i in article_name:
        if i not in string.punctuation:
            article_name_beauty += i
        else:
            article_name_beauty += ''
    article_name_beauty = article_name_beauty.replace('  ', ' ').replace(' ', '_') + '.txt'
    return article_name_beauty


for article in all_articles:
    article_meta = {}
    if article.find('span', 'c-meta__type').text == 'News':
        article_meta['tag'] = article.find('span', 'c-meta__type').text
        article_meta['url'] = article.find('a', 'c-card__link u-link-inherit')['href']
        article_meta['header'] = article.find('a', 'c-card__link u-link-inherit').text
        nature_news.append(article_meta)

for news in nature_news:
    filename = generate_filename(news['header'])
    file = open(filename, 'w', encoding='utf-8')
    url_post = news['url']
    article = requests.get(base_url + url_post)
    article_soup = BeautifulSoup(article.content, 'html.parser')
    article_body = article_soup.find('div', {'class': "c-article-body"}).text.strip()
    for p in article_body:
        file.write(p)
    file.close()
