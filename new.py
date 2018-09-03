from scraper_hb import get_data
from crontab import CronTab
import sys
import boto3
from boto3.dynamodb.conditions import Attr
import datetime

now = datetime.datetime.now()


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


if not sys.argv[1]:
    print("url needed")
    exit()

result = get_data(sys.argv[1])

if "not found" in result:
    print("please use hb, n11 or gg url")
    exit()

if check_if_new(result['productId']):
    print('NEW product: ' + result['productId'])
    my_cron = CronTab(user='emingure')
    cmd = '/usr/local/bin/python3 ~/tmp/shopping-tracker/worker.py ' + sys.argv[1]
    job = my_cron.new(command=cmd, comment=result['productId'])
    job.minute.on(now.minute)
    job.hour.on(now.hour)
    my_cron.write()
