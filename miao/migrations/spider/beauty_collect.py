import urllib.request
from bs4 import BeautifulSoup


def collect():
    response = urllib.request.urlopen("http://www.bishijie.com/kuaixun/")
    print(response.read().decode('utf-8'))
    doc = response.read().decode('utf-8')
    soup = BeautifulSoup(doc, 'html.parser', from_encoding='utf-8')
    node = soup.find_all('li', class_='lh32')
    print(node)
