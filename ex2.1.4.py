#!/usr/bin/env python

####Dictionaries

#initialize a few dictionaries with {}
names = {
	'aaron': 'hardin','mike' : 'lawson','peter': 'combs'
}

drinks = {
    'mike': 'coffee', 'aisha': 'beer', 'peter':'soda'
}

wines = {
	'red': 'cabernet', 'white': 'pinot grigio', \
	'sparkling': 'blanc de noirs', 'sticky': 'muscato'
}

#print dictionaries
print names
print drinks
print wines
print

#find a value
print names['aaron']
print drinks['peter']
print wines['sparkling']
print

######
#####adding to the dictionary
#add single item
drinks['debbie'] = 'diet coke'
print drinks
print

#combine two dictionaries
print names
print drinks
names.update(drinks)
print names
print

#shrinking the dictionary
del names['aaron']
print names
print

#changing dictionaries in place
#modify items in dictionary
names['nate'] = 'krefman'
print names
print

#characterizing dictionaries
#identify components of a list
#1) The dictionary methods keys() and values() return lists contain 
#keys or values. These lists can be stored and acted on as lists.
keys = wines.keys()
values = wines.values()
print keys
print values
print

#iterate over keys
#2) We can iterate over the keys and print the values
# using the syntax for x in [ ]:
for x in keys:
	print "The category is", x, "and the varietal is", wines[x]

print

#find if something is stored
#3) We can quickly find out if a particular key already exists. 
#Note that each key must be unique, but multiple keys can have the same value.
if 'red' in wines: print wines['red']
print
print










































