from scraper_hb import get_data
from crontab import CronTab
import sys
import boto3
from boto3.dynamodb.conditions import Attr
import datetime



def check_if_new(pId):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('stocks')

    response = table.scan(
        FilterExpression=Attr('productId').eq(pId)
    )

    items = response['Items']
    # print(items)

    if len(items) == 1:
        return True

    return False


def crawl(url):
    if not url:
        print("url needed")
        exit()

    result = get_data(url)

    if "not found" in result:
        print("please use hb, n11 or gg url")
        exit()

    now = datetime.datetime.now()

    if check_if_new(result['productId']):
        print('NEW product: ' + result['productId'])
        my_cron = CronTab(user='crons')
        cmd = '/usr/bin/python3 /home/shopping-tracker/worker.py ' + url
        job = my_cron.new(command=cmd, comment=result['productId'])
        job.minute.on(now.minute)
        job.hour.on(now.hour)
        my_cron.write()

    return result
