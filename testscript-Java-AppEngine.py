import re
import urllib.request
from bs4 import BeautifulSoup

numbers = []
nonuniques = 0
for k in range(1000):
    html = urllib.request.urlopen('https://randomnumbergeneratorclean.appspot.com')
    soup = BeautifulSoup(html, features="html.parser")
    data = soup.findAll(text=True)
     
    def visible(element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False
        return True
     
    result = filter(visible, data)
    for i in list(result):
        if i.isdigit():
            print(k,': ',i)
            numbers.append(i)

for j in range(len(numbers)):
    for l in range(len(numbers)):
        if j == l:
            ++nonuniques
            print('Nonuniques: ', nonuniques)
