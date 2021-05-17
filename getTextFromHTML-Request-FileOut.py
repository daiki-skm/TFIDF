import requests
import sys
import webbrowser
import bs4
import codecs

res = requests.get('http://www.u-aizu.ac.jp')
status_code = res.status_code

# print('encoding = ', res.encoding)
# text = res.text
# print('Status: ', status_code)
# print('Contents: ', text)

# print(res.content)

content_type_encoding = res.encoding if res.encoding != 'ISO-8859-1' else None
bs = bs4.BeautifulSoup(res.content, 'html.parser', from_encoding=content_type_encoding)

for i in bs.select('body'):
  print(i.getText())

# Save to file
with open('NLTK-Tag-PY/outcontents.txt', 'w') as outf:
  for i in bs.select('body'):
    print(i.getText(), file=outf)
outf.close()
