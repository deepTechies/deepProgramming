# This is to calculate the best score

bestScore = 0
file = open ("results.txt")
for i in file:
    if float(i) > bestScore:
        bestScore = float(i)
close.file()
print("The best score is: ")
print (bestScore)
