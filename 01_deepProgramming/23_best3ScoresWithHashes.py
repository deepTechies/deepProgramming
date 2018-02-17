# This is to calculate the best score

scores = {}
file = open ("results.txt")
for line in file:
    (name, score) = line.split()  
    scores[score] = name
file.close() 
for eachScore in scores.keys():
    print ("Surfer " + scores[eachScore] + " has scored " + eachScore)
