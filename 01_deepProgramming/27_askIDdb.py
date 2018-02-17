# This is to look for profiles with an id
# p is for profile!

import sqlite3
# First, define a function
def findDetails(findId):
    db = sqlite3.connect("surfing_data.csv")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("select * from surfers")
    rows = cursor.fetchall()
    for row in rows:
        if row['id'] == findId:
            p = {}
            p['id'] = str(row['id'])
            p['name'] = row['name']
            p['country'] = row['country']
            p['average'] = str(row['average'])
            p['board'] = row['board']
            p['age'] = str(row['age'])
            cursor.close()
            return(p)
    cursor.close()
    return({})

# Tester code of the above function
lookupId =  int(input("Enter the id of the surfer: "))
surfer = findDetails(lookupId)

if surfer: 
    print("ID:         " + surfer['id'])                                                 
    print("Name:       " + surfer['name']) 
    print("Country:    " + surfer['country']) 
    print("Average:    " + surfer['average']) 
    print("Board type: " + surfer['board']) 
    print("Age:        " + surfer['age'])
