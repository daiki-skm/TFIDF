import requests
 
url = 'https://it-engineer-lab.com/feed'

try:
    r = requests.get(url)
    with open('rss.xml', mode='w') as f:
        f.write(r.text)
except requests.exceptions.RequestException as err:
    print("Writing error: " + err)

f.close()
