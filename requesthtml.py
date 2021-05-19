import requests
import bs4


def get_article() -> None:
    # res = requests.get('http://www.u-aizu.ac.jp')
    # res = requests.get('https://www.nytimes.com/section/sports/basketball')
    res = requests.get('https://golang.org/doc/')

    # status_code = res.status_code
    # print('encoding = ', res.encoding)
    # text = res.text
    # print('Status: ', status_code)
    # print('Contents: ', text)
    # print(res.content)

    content_type_encoding = res.encoding if res.encoding != 'ISO-8859-1' else None
    bs = bs4.BeautifulSoup(res.content, 'html.parser', from_encoding=content_type_encoding)

    # Save to file
    with open('outcontents.txt', 'w') as outf:
         for i in bs.select('body'):
            outf.write(i.getText())
    outf.close()
