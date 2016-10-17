from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

#html = urlopen("http://pythonscraping.com/pages/page1.html")
#print(html.read())

#html = urlopen("http://pythonscraping.com/pages/page1.html")
#bsObj = BeautifulSoup(html.read(), "html.parser")
#print(bsObj.h1)

'''
try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print("Unable to find server.")
else:
    print("Success")
'''
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("No title found")
else:
    print(title)
