import urllib.request
from bs4 import BeautifulSoup
import json

response = urllib.request.urlopen('https://www.db.com/news/detail/20230317-deutsche-bank-reports-continued-delivery-of-transformation-in-2022-and-clear-targets-for-2025?language_id=1')

html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')

article_text=soup.find("div",{"class":"rich-text"})
                       
print (article_text.text)   
