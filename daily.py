import requests
from lxml import html
import time
from new import crawl
import sys




def gittigidiyor():
    url = "https://www.gittigidiyor.com/super-firsatlar/gunun-firsati/yildiz-firsatlar"
    r = requests.get(url)
    root = html.fromstring(r.content)

    urls = root.xpath('//*[@id="daily-deal-product-container"]/div/div[2]/div/a')

    for url in urls:
        print("crawling started: " + url.get('href'))
        crawl('http:'+url.get('href'))




def n11():
    url = "https://www.n11.com/super-firsatlar"
    r = requests.get(url)
    root = html.fromstring(r.content)

    urls = root.xpath('//*[@id="contentDailyDeal"]/div/div[3]/div/div/ul/li/div/div[1]/a[1]')
    # print(len(urls))
    for url in urls:
        print("crawling started: " + url.get('title'))
        crawl(url.get('href'))
        time.sleep(3)



def hepsiburada():
    url = "https://www.hepsiburada.com/gunun-firsati-teklifi"
    r = requests.get(url)
    root = html.fromstring(r.content)

    urls = root.xpath('//*[@class="deal-of-the-day-list"]//*/a')
    # print(len(urls))
    for url in urls:
        print("crawling started: " + url.get('href'))
        crawl('https://www.hepsiburada.com/'+url.get('href'))
        time.sleep(3)


def daily_run(site):
    if site == 'hepsiburada':
        hepsiburada()
    elif site == 'gittigidiyor':
        gittigidiyor()
    elif site == 'n11':
        n11()
    else:
        print("Invalid site")

if len(sys.argv)<2:
    print("Please add a site parameter")
    exit()

daily_run(sys.argv[1])
# print(sys.argv[1])
