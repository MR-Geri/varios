# Задание 4 - peak.html http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=peak.html
import requests
from bs4 import BeautifulSoup


URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=90231'


def get_html(url, params=None):
    r = requests.get(url, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    # items = soup.find_all('a', class_='na-card-item')
    return soup


def parse():
    global URL
    html = get_html('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=90231')
    while html.status_code == 200:
        data = str(get_content(html.text))
        u = URL.split('=')
        URL = f'{u[0]}={data.split()[-1]}'
        print(data, URL)
        html = get_html(URL)
