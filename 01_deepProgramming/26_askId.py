# This is to look for profiles with an id
# p is for profile!

# First, define a function
def findDetails(findId):
    file = open ("surfing_data.csv")
    for line in file:
        p = {}
        (p['id'], p['name'], p['country'], p['average'], p['board'], p['age']) = line.split(";")
        if findId == int(p['id']):
            file.close() 
            return(p)
    file.close()
    return({})

# Tester code of the above function
lookupId =  int(input("Enter the id of the surfer: "))
surfer = findDetails(lookupId)

if surfer:
    print ("ID:          "+surfer['id'])
    print ("Name:        "+surfer['name'])
    print ("Country:     "+surfer['country'])
    print ("Average:     "+surfer['average'])
    print ("Board:       "+surfer['board'])
    print("Age:          "+surfer['age'])

