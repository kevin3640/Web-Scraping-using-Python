from bs4 import BeautifulSoup 
from selenium import webdriver
import pandas as pd
import lxml

driver = webdriver.Chrome("chromedriver.exe")
products=[] 
prices=[] 
styles=[]

for page in range(1, 5):
    driver.get("https://www.myntra.com/men-tshirts?p=" + str(page))
    content = driver.page_source
    soup = BeautifulSoup(content,'lxml')
    for a in soup.findAll(attrs={'class':'product-base'}):
        name=a.find(attrs={'class':'product-brand'})
        price=a.find(attrs={'class':'product-price'})
        style=a.find(attrs={'class':'product-product'})
        products.append(name.text)
        prices.append(price.text)
        styles.append(style.text)
        
df = pd.DataFrame({'Product Name':products,'Style':styles,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')