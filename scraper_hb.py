import urllib.request
import requests
from lxml import etree, html
import time


url="https://www.hepsiburada.com/prima-bebek-bezi-premium-care-3-beden-midi-aylik-firsat-paketi-204-adet-p-HBV000005KOL5"

def get_price(url):
    # #url = "https://byv.org.tr"
    reaction = urllib.request.urlopen(url)
    # time.sleep(5)
    htmlparser = etree.HTMLParser()
    tree = etree.parse( reaction, htmlparser)
    # a = tree.xpath( '//*[@id="duyuru-arka"]/a[1]/div[1]')
    # print(a[0].text)

    r = requests.get(url)
    root = html.fromstring(r.content)
    title = root.xpath('/html/body/script[2]')
    # print("My blog title is: '{}'".format(title[0].text))
    data = title[0].text

    import json
    import re
    # from bs4 import BeautifulSoup
    #
    # web = urllib.request.urlopen(url)
    # soup = BeautifulSoup(web.read(), 'lxml')
    # data  = soup.find_all("script")#.string
    # print(data)
    p = re.search(r'var productModel = (.*);', data)
    # m = p.match(data)
    a = json.loads(p.group(1))
    # print(p.group(1))
    return a['product']['currentListing']['currentPrice']['value']
    #
    #
    # # body > script:nth-child(7)
