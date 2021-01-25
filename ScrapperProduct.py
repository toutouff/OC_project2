import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

reponse = requests.get(url)

if reponse.ok:

    soup = BeautifulSoup(reponse.text, features='html.parser')
    title = soup.find('h1').text
    table = soup.find('table', class_='table table-striped')
    td = table.find_all('td')
    upc = td[0].text
    priceeExTax = td[2].text
    priceIncTax = td[3].text
    nbrAiv = td[5].text
    productPageUrl = url
    productdescription = ''
    body = soup.find('body', class_='default')
    allP = soup.findAll('p')
    productdescription = allP[3].text
    print(productdescription)
