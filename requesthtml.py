import requests
import bs4


def get_article() -> None:
    url_arr = [
        'https://golang.org/doc/',
        'https://time.com/6050639/nba-covid19/',
        'https://time.com/6049687/tokyo-olympics-cancel-doctors/',
        'https://www.bbc.com/news/uk-politics-57198607',
        'https://www.bbc.com/news/business-57154345',
        'https://www.bbc.com/news/business-57171683',
    ]

    flag = 0

    for url in url_arr:
        res = requests.get(url)
        # status_code = res.status_code
        # print('encoding = ', res.encoding)
        # text = res.text
        # print('Status: ', status_code)
        # print('Contents: ', text)
        # print(res.content)

        content_type_encoding = res.encoding if res.encoding != 'ISO-8859-1' else None
        bs = bs4.BeautifulSoup(res.content, 'html.parser', from_encoding=content_type_encoding)

        # Save to file
        if flag == 1:
            with open('outcontents.txt', 'a') as outf:
                for i in bs.select('body'):
                    print(i.getText(), file=outf)
            outf.close()
        else:
            with open('outcontents.txt', 'w') as outf:
                for i in bs.select('body'):
                    print(i.getText(), file=outf)
            outf.close()
            flag = 1

# get_article()
