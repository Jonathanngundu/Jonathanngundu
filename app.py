import sys 
import requests
from bs4 import BeautifulSoup
import time 

def steer():
    URL = 'https://www.incredible.co.za/vx-gaming-precision-drive-series-steering-wheel'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

    page = requests.get(URL, headers=headers)


    soup =  BeautifulSoup(page.content, 'html.parser')

    price = soup.find(class_="price").get_text()
    price_x = price.replace('R', '')
    price_0 = price_x.replace(',', '')
    price_final = float(price_0)
    print(price_final)

    if 1499 > price_final:
       print("don't but buy")
    else:
       print("buy now ")



while(True):
    
    steer()
    time.sleep(200)