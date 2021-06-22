import requests
import bs4
from newsapi import NewsApiClient
import os


def get_article() -> None:
    newsapi = NewsApiClient(api_key='c8ac3154f53c47cb992f106527e9cd51')

    p_data = newsapi.get_top_headlines(category='business')
    n_data = newsapi.get_top_headlines(category='sports')

    p_url_arr = []
    n_url_arr = []

    for article in p_data['articles']:
        p_url_arr.append(article['url'])

    for article in n_data['articles']:
        n_url_arr.append(article['url'])

    print("p_data url total num", len(p_url_arr))
    print("n_data url total num", len(n_url_arr))

    os.remove('nData.txt')
    os.remove('pData.txt')

    for url in p_url_arr:
        if url == 'https://www.straitstimes.com/business/companies-markets/bitcoin-tumbles-further-as-china-tightens-crypto-crackdown':
            continue
        res = requests.get(url)
        if res.status_code == 403:
            continue

        # print('encoding = ', res.encoding)
        # print('Status: ', res.status_code)
        # print('Contents: ', res.text)
        # print(res.content)

        content_type_encoding = res.encoding if res.encoding != 'ISO-8859-1' else None
        bs = bs4.BeautifulSoup(res.content, 'html.parser', from_encoding=content_type_encoding)

        # Save to file
        with open('pData.txt', 'a') as outf:
            for i in bs.select('body'):
                text = i.getText()
                text = text.replace("\n", "")
                text = " ".join(text.split())
                print(text, file=outf)
        outf.close()

    for url in n_url_arr:
        res = requests.get(url)

        if res.status_code == 403:
            continue

        content_type_encoding = res.encoding if res.encoding != 'ISO-8859-1' else None
        bs = bs4.BeautifulSoup(res.content, 'html.parser', from_encoding=content_type_encoding)

        # Save to file
        with open('nData.txt', 'a') as outf:
            for i in bs.select('body'):
                text = i.getText()
                text = text.replace("\n", "")
                text = " ".join(text.split())
                print(text, file=outf)
        outf.close()

# get_article()
