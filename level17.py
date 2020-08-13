import xmlrpc.client
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote_to_bytes
import bz2


def get_html(url, auth=('huge', 'file')):
    r = requests.get(url, auth=auth)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def parse(url):
    info = ''
    html = get_html(url)
    while html.status_code == 200:
        try:
            data = str(get_content(html.text))
            u = url.split('=')
            URL = f'{u[0]}={data.split()[-1]}'
            info += html.cookies['info']
            print(data, URL, html.cookies['info'])
            html = get_html(URL)
        except:
            return info


# data = parse('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345')
data = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'
data = unquote_to_bytes(data.replace("+", " "))
print(bz2.decompress(data).decode())
url = 'http://www.pythonchallenge.com/pc/phonebook.php'
print(xmlrpc.client.ServerProxy(url).phone("Leopold"))
print(requests.get('http://www.pythonchallenge.com/pc/stuff/violin.php',
                   cookies={'info': 'the flowers are on their way'}).text)
# balloons
# http://www.pythonchallenge.com/pc/return/balloons.html
