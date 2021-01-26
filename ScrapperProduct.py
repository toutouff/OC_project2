import requests
from bs4 import BeautifulSoup

class Page(object):

    def __init__(self, url):
        self.url = url

class ProductPage(Page):

    def reponse(self):
        reponse = requests.get(self.url)
        self.soup = BeautifulSoup(reponse.text, features='html.parser')
        return reponse

    def getTitle(self):
        title = self.soup.find('h1').text
        self.title = title

    def getInfo(self):
        self.reponse()
        table = self.soup.find('table',class_='table table-striped')
        td = table.findAll('td')
        self.upc = td[0].text
        self.priceeExTax = td[2].text
        self.priceIncTax = td[3].text
        self.nbrAiv = td[5].text
        self.getTitle()
        self.getProductDescription()

    def getProductDescription(self):
        allP = self.soup.findAll('p')
        self.productdescription = allP[3].text

    def getImg(self):
        row = self.soup.find_all('div' , class_='col-sm-6')
        img = row[0].find('img')
        self.img = img['src']



productpage = ProductPage("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
productpage.getInfo()
productpage.getRow()
