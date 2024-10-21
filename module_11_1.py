#from PIL import Image
#from bs4 import BeautifulSoup
#from html.parser import HTMLParser
import re
from urllib.request import urlopen
import urllib.request

from urllib3 import request

sf = 'img src="'
url = "https://.ru"
U = urlopen(url)
im_list = []
for s in U:
    s = str(s)
    i = s.find(sf)
    if i > -1:
        for line in s.split('\n'):
            im_list.append(''.join(re.findall(r'"[^\"]+[https]"', line)))
            url = ''.join(re.findall(r'"[^\"]+[https]"', line))
            print(url)
            img = urllib.request.urlopen(url).read()
           # out = open("img.jpg", "wb")
           # out.write(img)
           # out.close
print(im_list)



#parser.feed(U)
#print(print(U.read()))
