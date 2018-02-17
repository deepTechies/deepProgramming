from transactions import *
import promotions
import starbuzz

items = ["Salad", "Coffee", "Donuts", "Cereal"]
prices = [1.50, 2.0, 1.80, 1.20]
running = True

while running:
    option = 1
    for choice in items:
        print(str(option)+"."+choice)
        option =  option + 1
    print(str(option) + ".Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
        runnning = False
    else:
        creditCard = input("Enter your credit card number: ")
        newPrice = promotions.discount(prices[choice-1])        
        if input("Starbuzz card? ") == "Y":
            newPrice = starbuzz.discount(newPrice)
    saveTransaction(newPrice, creditCard, items[choice - 1])
