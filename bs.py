import requests
import bs4
import re
from time import sleep


keywords = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='html.parser')
sleep(1)

titles = soup.select('div.tm-article-snippet')

links = []
for title in titles:
    link = 'https://habr.com' + title.select_one('a.tm-title__link')['href']
    links.append(link)

for link in links:
    response = requests.get(link)
    soup = bs4.BeautifulSoup(response.text, features='html.parser')
    sleep(1)
    article_text = soup.select('p')
    article_date = soup.select_one('time')['datetime']
    article_title = soup.select_one('h1').text
    text_string = ''.join(str(elem) for elem in article_text)

    for word in keywords:
        if re.search(word, text_string, re.IGNORECASE):
            print(article_date)
            print(article_title)
            print(link)
            print()
