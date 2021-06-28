from newsapi import NewsApiClient


def get_url() -> None:
    newsapi = NewsApiClient(api_key='c8ac3154f53c47cb992f106527e9cd51')

    p_data = newsapi.get_top_headlines(category='business')
    n_data = newsapi.get_top_headlines(category='sports')

    with open('pUrl.txt', 'a') as outf:
        for article in p_data['articles']:
            print(article['url'], file=outf)
    outf.close()

    with open('nUrl.txt', 'a') as outf:
        for article in n_data['articles']:
            print(article['url'], file=outf)
    outf.close()

get_url()
