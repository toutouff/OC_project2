import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
linkStart = 'http://books.toscrape.com/catalogue/category/'
reponse = requests.get(url)

i = 0

if reponse.ok:
    links = []
    categories = []

    soup = BeautifulSoup(reponse.text, features="html.parser")
    sideCategories = soup.find('div', class_='side_categories')
    ul = sideCategories.findAll('li')
    for li in ul:
        a = li.find('a')
        categorie = str(li.text)
        categorie = categorie.replace('\n', '')
        categorie = categorie.replace(' ', '')
        categories.append(categorie + ' ;\n')
        link = str(a['href'])
        if i == 0:
            link = 'books_1/' + link
            i = i + 1
        links.append(linkStart + link.replace("../", "", 1))

indexedlinks = []
enumLinks = enumerate(links)
for link in enumLinks:
    indexedlink = list(link)
    indexedlinks.append(indexedlink)

for link in indexedlinks:
    reponse = requests.get(link[1])
    soup = BeautifulSoup(reponse.text, features="html.parser")
    li = soup.find('li', class_=('next'))
    if li != None:
        a = li.find('a')
        href = a['href']
        isNextButton = True
        url = link[1]
        url = url.replace('index.html', str(href))
        links.insert(link[0], url)
print(links)
