import urllib.request
import time

def send_to_twitter(msg):
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API", "http://twitter.com/statuses", "...", "...")
    http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params = urllib.parse.urlencode( {'status': msg} )
    resp = urllib.request.urlopen("http://twitter.com/statuses/update.json", params)
    resp.read()

def get_price():
    page = urllib.request.urlopen("http://ww1.beans-r-us.biz/prices.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    startOfPrice = where+2
    endOfPrice = startOfPrice+4
    return(float[startOfPrice:endOfPrice])

priceNow = input("Do you want the coffee now (Y/N)?")
if priceNow == "Y":
	send_to_twitter(get_price())
else:  
    price = 99.99
    while price > 4.74:
        time.sleep(900)
        price = get_price()
        send_to_twitter("Buy!")
