import requests
from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep
import winsound




headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
url67=requests.get("https://www.amazon.in/GIGABYTE-GeForce-Windforce-DisplayPort-GV-N166TOC-6GD/dp/B07NJPKZQG/ref=dp_prsubs_1?pd_rd_i=B07NJPKZQG&psc=1",headers=headers)
soup = BeautifulSoup(url67.content, features="lxml")
title = soup.find(id="productTitle").get_text().strip()
print(title)
item=0
while True:
    try:
        price = soup.find(id='priceblock_ourprice').get_text().replace('₹', '').strip().split(",")
        price="".join(price)
        price=float(price)
        if price<48000:
            duration = 500  # milliseconds
            freq = 440  # Hz
            winsound.Beep(freq, duration)
            print(price) 
    #print(price)
    except:
        print("nothing to look for")
    
    



#print("nothing")
                # this part gets the price in dollars from amazon.com store
              #  try:
             #       price = float(soup.find(id='priceblock_saleprice').get_text().replace('$', '').replace(',', '').strip())
              #  except:
              #      price = ''
#url.
#//*[(@id = "buybox-see-all-buying-choices")]//*[contains(concat( " ", @class, " " ), concat( " ", "a-button-text", " " ))]
#
#
#₹48,293.00
#48293.00
