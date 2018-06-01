from lxml.html import soupparser
import bs4

def getHref(html):
    soup = bs4.BeautifulSoup(html, 'lxml')
    for tr in soup.find_all(id="form2"):
        return tr.a.get('href')

def isCompleted(html):
    soup = bs4.BeautifulSoup(html, 'lxml')
    return soup.find("td", text="[Kuesioner sudah dilakukan]")

def getUrl(content):
    root = soupparser.fromstring(content)
    result_url = root.xpath('//meta[@http-equiv="refresh"]/@content')
    if result_url:
        result_url = str(result_url[0])
        urls = result_url.split('URL=') if len(result_url.split('url=')) < 2    else result_url.split('url=')
        url = urls[1] if len(urls) >= 2 else None
    else:
        return None
    return url