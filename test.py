import sys 
import requests
from bs4 import BeautifulSoup
import time 
import pyttsx3

def steer():
    engine = pyttsx3.init()
    URL = 'https://www.incredible.co.za/vx-gaming-precision-drive-series-steering-wheel'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

    page = requests.get(URL, headers=headers)


    soup =  BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="product-price-86488").get_text()
    price_r = price.replace('R', '')
    price_c = price_r.replace(',', '')
    price_final = float(price_c)
    print(price_final)

    if 1499 < price_final:
       print("don't but buy")
    else:
       print("buy now ")
       engine.say("but the product now")
       engine.runAndWait()



while(True):
    
    steer()
    time.sleep(200)