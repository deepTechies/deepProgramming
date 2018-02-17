def saveTransaction(price, creditCard, description):
    file = open("transactions.txt", "a")
    file.write("%16s%07d%16s\n" % (creditCard, price*100, description))
    file.close()
