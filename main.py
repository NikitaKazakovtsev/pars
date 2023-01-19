import re
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import pprint



HOST = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

def get_headers():
    g = Headers(browser='firefox', os='win').generate()
    return g

articles = []

vacancy = requests.get(HOST, headers=get_headers()).text
soup = BeautifulSoup(vacancy, features='lxml')
article_list_tag = soup.find(id="a11y-main-content")
list_1 = article_list_tag.find_all(class_="serp-item")

for vacancy in list_1:
    vacancy_link = vacancy.find(class_="serp-item__title")['href']
    vacancy1 = requests.get(vacancy_link, headers=get_headers()).text
    soup1 = BeautifulSoup(vacancy1, features='lxml')
    asd = soup1.find(class_="vacancy-title")
    asd1 = asd.find('span')
    money = asd1.text
    company = vacancy.find('a', attrs={"data-qa": "vacancy-serp__vacancy-employer"}).text
    town = vacancy.find('div', attrs={"data-qa": "vacancy-serp__vacancy-address"}).text
    description = vacancy.find(class_="g-user-content").text
    if  "Django" in description and "Flask" in description:
        articles.append({
            'link': vacancy_link,
            'company': company,
            'money': money,
            'town': town,
            'description':description

        })
print(articles)

#soup.find('span', attrs={"data-qa": "vacancy-serp__vacancy-compensation"})