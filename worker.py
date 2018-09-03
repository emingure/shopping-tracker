from scraper_hb import get_data
import sys

if not sys.argv[1]:
    print("url needed")
    exit()

result = get_data(sys.argv[1])

if "not found" in result:
    print("please use hb, n11 or gg url")
    exit()

print(result)
