# This is to calculate the best score

#bestScore = 0
scores = []
file = open ("results.txt")
for i in file:
    (name, score) = i.split()  
    scores.append(score) 
scores.sort()
scores.reverse()
file.close()
print ("The top scores are: ")
print(scores[0])
print(scores[1])
print(scores[2])
