import requests, string, os
from bs4 import BeautifulSoup

page_cnt = int(input())
article_category = input()
base_url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page='
article_url = 'https://www.nature.com'
articles_to_file = []


def generate_filename(article_name):
    article_name_beauty = ''
    for i in article_name:
        if i not in string.punctuation:
            article_name_beauty += i
        else:
            article_name_beauty += ''
    article_name_beauty = article_name_beauty.replace('  ', ' ').replace(' ', '_') + '.txt'
    return article_name_beauty


def populate_articles_meta(url, category, page):
    r = requests.get(url + str(page), headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(r.content, 'html.parser')
    all_articles = soup.find_all('li', 'app-article-list-row__item')
    for article in all_articles:
        article_meta = {}
        if article.find('span', 'c-meta__type').text == category:
            article_meta['page'] = page
            article_meta['tag'] = article.find('span', 'c-meta__type').text
            article_meta['url'] = article.find('a', 'c-card__link u-link-inherit')['href']
            article_meta['header'] = article.find('a', 'c-card__link u-link-inherit').text
            articles_to_file.append(article_meta)


for scraper in range(page_cnt):
    try:
        os.mkdir('Page_' + str(scraper + 1))
    except FileExistsError:
        print('Directory already created')
    populate_articles_meta(base_url, article_category, scraper + 1)

for note in articles_to_file:
    filename = generate_filename(note['header'])
    file = open('Page_' + str(note['page']) + '/' + filename, 'w', encoding='utf-8')
    url_post = note['url']
    article = requests.get(article_url + url_post)
    article_soup = BeautifulSoup(article.content, 'html.parser')
    article_body = article_soup.find('div', {'class': "c-article-body"}).text.strip()
    for p in article_body:
        file.write(p)
    file.close()
