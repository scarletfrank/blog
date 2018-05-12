import urllib.request
class MyOpener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
openurl = MyOpener().open
url = 'http://scholar.google.se/scholar?hl=en&q=zh+zhan'
openurl(url).read()
from bs4 import SoupStrainer, BeautifulSoup
page = BeautifulSoup(openurl(url).read(), parse_only=SoupStrainer('div', id='gs_ab_md'))
