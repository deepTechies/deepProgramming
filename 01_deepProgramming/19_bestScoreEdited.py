# This is to calculate the best score

bestScore = 0
file = open ("results.txt")
for i in file:
    (name, score) = i.split()
    if float(score) > bestScore:
        bestScore = float(score)
file.close()
print ("The best score is: ")
print(bestScore)
