import requests
import bs4
import os


def get_article() -> None:
    with open('pUrl.txt', encoding="utf-8_sig") as fp:
        p_url_arr = fp.readlines()

    with open('nUrl.txt', encoding="utf-8_sig") as fp:
        n_url_arr = fp.readlines()

    print("p_data url total num", len(p_url_arr))
    print("n_data url total num", len(n_url_arr))

    # os.remove('nData.txt')
    # os.remove('pData.txt')

    for url in p_url_arr:
        res = requests.get(url.replace('\n', ''))
        if res.status_code == 403:
            continue

        # print(url)

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
                if text == "Access Denied":
                    continue
                print(text, file=outf)
        outf.close()

    for url in n_url_arr:
        res = requests.get(url.replace('\n', ''))
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
                if text == "Access Denied":
                    continue
                print(text, file=outf)
        outf.close()


get_article()
