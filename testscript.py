import re
import urllib.request
import math
from bs4 import BeautifulSoup

numbers = []
fails = 0
logfile = open("test_log.txt","w+")
for f in range(10):
    nonuniques = 0
    for k in range(1000):
        html = urllib.request.urlopen('https://randomnumbergeneratorclean.appspot.com/')
        soup = BeautifulSoup(html, features="html.parser")
        data = soup.findAll(text=True)
         
        for i in list(data):
            if i.isdigit():
                print(k,': ',i)
                numbers.append(i)

    for j in range(len(numbers)):
        for l in range(len(numbers)):
            if j == l:
                ++nonuniques
                print('Nonuniques: ', nonuniques)
    nonuniques = math.ceil(nonuniques/2)
    if nonuniques > 250:
        ++fails
logfile.write("750/1000 Unique Test Fails: ")
logfile.write(str(fails))
logfile.close()
