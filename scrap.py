## Imports
import requests
import bs4
from bs4 import BeautifulSoup


class Scrap:
    def __init__(self, url):
        self.url = url

    def scrap_urls_from_page(self):
        r = requests.get(self.url)
        htmlContent = r.content
        soup = BeautifulSoup(htmlContent, "html.parser")
        contentTable = soup.select('ul li a')
        for i in contentTable:
            print(i)
