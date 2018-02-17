# This is to calculate the best score

#bestScore = 0
scores = []
names = []
file = open ("results.txt")
for i in file:
    (name, score) = i.split()  
    scores.append(float(score))
    names.append(name)
file.close() 
scores.sort(reverse = True)
names.sort(reverse = True)
print ("The top scores are: ")
print(names[0] + " with " + str(scores[0]))
print(names[1] + " with " + str(scores[1]))
print(names[2] + " with " + str(scores[2]))
