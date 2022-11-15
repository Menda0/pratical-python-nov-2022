# 1. Use the csv module
# 2. Create csv file
# 3. In every line of the csv file you must write the number and fib(number)
# Docs - https://docs.python.org/3/library/csv.html

## Example ##
## fib(0), 0
## fib(1), 1
## fib(2), 1
## fib(3), 5
## ...
## fib(20), 

### Provided by Hugo  ###
import csv
import requests
from module_example.math import fib

with open('fib.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',') # quotechar='|', quoting=csv.QUOTE_MINIMAL)
    n = 0
    while n <= 20:
        spamwriter.writerow([f"fib({n})",fib(n)])
        n += 1

# ----

## https://api.spaceflightnewsapi.net/v3/articles
# 1. Use requests to get a list of space news
# 2. Write all the news inside a csv file
# 3. ID, title, imageUrl, summary, url

### Provided by Augusto Fonseca ###
url = "https://api.spaceflightnewsapi.net/v3/articles"
http_response = requests.get(url)
space_news = http_response.json()

with open('exercice_7_news.csv', 'w', newline='', encoding='utf-8') as csvfile_news:
    spamwriter_news = csv.writer(csvfile_news, delimiter= ',', quotechar='"', quoting=csv.QUOTE_ALL)
    spamwriter_news.writerow(["ID","TITLE","IMAGE_URL","SUMMARY","URL"])
    for news in space_news:
        spamwriter_news.writerow([news['id'],news['title'],news['imageUrl'],news['summary'],news['url']])
