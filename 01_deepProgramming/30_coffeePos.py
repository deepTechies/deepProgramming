from transactions import *

items = ["Salad", "Coffee", "Donut", "Cereal"]
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
    saveTransaction(prices[choice - 1], creditCard, items[choice - 1])
