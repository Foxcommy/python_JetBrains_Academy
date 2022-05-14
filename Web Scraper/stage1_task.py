import requests, json

url = input('Input the URL:')


def quote_search(quote_url):
    r = requests.get(quote_url)
    if r and 'content' in r.json():
        print(r.json()['content'])
    else:
        print('Invalid quote resource!')


quote_search(url)
