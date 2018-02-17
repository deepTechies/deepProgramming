# This is to calculate the best score
# p for profile!
p = {}

line = "101;Johnny 'wave-boy' Jones;USA;8.32;Fish;21"
(p['id'], p['name'], p['country'], p['average'], p['board'], p['age']) = line.split(";")
print ("ID:          "+p['id'])
print ("Name:        "+p['name'])
print ("Country:     "+p['country'])
print ("Average:     "+p['average'])
print ("Board:       "+p['board'])
print("Age:          "+p['age'])

