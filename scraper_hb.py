import urllib.request
import requests
from lxml import etree, html
import time
import json
import re
from urllib.parse import urlparse



# url="https://www.hepsiburada.com/prima-bebek-bezi-premium-care-3-beden-midi-aylik-firsat-paketi-204-adet-p-HBV000005KOL5"
# url = "https://urun.n11.com/fritoz/tefal-actifry-original-1-kg-beyaz-fritoz-P237805653"
# url = "https://urun.gittigidiyor.com/bilgisayar-tablet/navitech-neotab-s130-10-1-10-ips-tablet-bilgisayar-305535198?scrf=haftanin-cok-satanlari"
url = "https://byv.org.tr"


def hepsiburada(url):

    r = requests.get(url)
    root = html.fromstring(r.content)
    title = root.xpath('/html/body/script[2]')
    data = title[0].text

    p = re.search(r'var productModel = (.*);', data)
    data = json.loads(p.group(1))
    listings = []
    stock = 0
    for listing in data['product']['listings']:
        listings.append(
                        {
                            'store': listing['merchantName'],
                            'price': listing['price']['amount'],
                            'url': 'https://www.hepsiburada.com' + listing['merchantVariantUrl'],
                            'stock': listing['quantity']

                        }
                        )
        stock += listing['quantity']
    return {'productId': data['product']['productId'],
            'url': url,
            'name': data['product']['name'],
            'brand': data['product']['brand'],
            'definition': data['product']['definitionName'],
            'seller': data['product']['currentListing']['merchantName'],
            'price': data['product']['currentListing']['currentPrice']['value'],
            'originalPrice': data['product']['currentListing']['pricing']['listingPriceList'][0]['value'],
            'listings': listings,
            'stock': stock }


def n11(url):

    r = requests.get(url)
    root = html.fromstring(r.content)

    div = root.xpath('//*[@class="stockCount"]')
    stock = div[0].value

    div = root.xpath('//*[@id="contentProDetail"]/div/aside/div[1]/div[1]/h3/a')
    seller = div[0].text

    div = root.xpath('//*[@id="contentProDetail"]/div/script[1]')
    data = div[0].text
    p = re.search(r'dataLayer.push\((.*)\);', data)
    data = json.loads(p.group(1))

    return {'productId': data['pId'],
            'url': url,
            'name': data['title'],
            'brand': data['pBrand'],
            'definition': data['pCat4'],
            'seller': seller,
            'originalPrice': data['pOriginalPrice'],
            'price': data['pDiscountedPrice'],
            'stock': stock }


def gittigidiyor(url):

    r = requests.get(url)
    root = html.fromstring(r.content)

    div = root.xpath('//*[@id="ProductDetails"]/meta[@itemprop="price"]')
    price = float(div[0].get('content'))

    div = root.xpath('//*[@class="price-css strike-price"]')
    if div:
        originalPrice = float(re.search(r'(.*) TL', div[0][0].text).group(1).replace(',','.'))
    else:
        originalPrice = price

    div = root.xpath('//*/meta[@itemprop="brand"]')
    brand = div[0].get('content')

    div = root.xpath('//*/meta[@itemprop="productId"]')
    productId = div[0].get('content')

    div = root.xpath('//*/meta[@itemprop="seller"]')
    seller = div[0].get('content')

    div = root.xpath('//*/meta[@itemprop="category"]')
    defi = div[0].get('content')


    div = root.xpath('/html/body/script[2]')
    data = div[0].text
    p = re.search(r'var TRACKING_PRODUCT_TITLE = \'(.*)\';', data)
    title = p.group(1)

    div = root.xpath('//*[@id="stockProduct"]')
    stock = int(div[0].value)


    return {'productId': productId,
            'url': url,
            'name': title,
            'brand': brand,
            'definition': defi,
            'seller': seller,
            'originalPrice': originalPrice,
            'price': price,
            'stock': stock }



def get_data(url):
    parsed = urlparse(url)
    host = parsed.hostname
    code = 200
    if 'gittigidiyor' in host:
        result = gittigidiyor(url)
    elif 'n11' in host:
        result = n11(url)
    elif 'hepsiburada' in host:
        result = hepsiburada(url)
    else:
        code = 404
        result = 'Method for "' + host + '" not found'

    print(code, result)

# get_data(url)

# print (hepsiburada(url))
# print (n11(url))
# print (gittigidiyor(url))
