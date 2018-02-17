import urllib.request
import time

def get_price():
    page = urllib.request.urlopen("http://ww1.beans-r-us.biz/prices.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    startOfPrice = where+2
    endOfPrice = startOfPrice+4
    return(float[startOfPrice:endOfPrice])

priceNow = input("Do you want the coffee now (Y/N)?")
if priceNow == "Y":
	print(get_price())
else:  
    price = 99.99
    while price > 4.74:
        time.sleep(900)
        price = get_price()
    print("Buy!")
