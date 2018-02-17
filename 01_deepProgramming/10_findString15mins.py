import urllib.request
import time

price = 99.99
while price > 4.74:
    time.sleep(900)
    page = urllib.request.urlopen("http://ww1.beans-r-us.biz/prices.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    
    startOfPrice = where+2
    endOfPrice = startOfPrice+4

    price= float(text[startOfPrice:endOfPrice])
    
print ("Buy!")
