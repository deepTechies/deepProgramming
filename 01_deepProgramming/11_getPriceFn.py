import urllib.request

def get_price():
    page = urllib.request.urlopen("http://ww1.beans-r-us.biz/prices.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    
    startOfPrice = where+2
    endOfPrice = startOfPrice+4

    print(text[startOfPrice:endOfPrice])
    
