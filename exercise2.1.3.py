####Getting to know your neighbors
print
print
#initialize a dictionary
fourthyears = {'Brock':'Nicole King', 'Robyn':'Andy Martin',
                'Margaux': 'Lin He', 'Nate':'David Drubin'}
print fourthyears
print

#print out the dictionary
for PhDcandidate in fourthyears:
	print "%s is indendured to %s" % (PhDcandidate, fourthyears[PhDcandidate])
print

# What happens if you try to index a non-existant key?
print fourthyears['Brock'] #this key exists so it will return a value
# print fourthyears['Terry'] # 'Terry' does not exist, error
print '-' * 20

#what happens if you try to assign a non-existant key?
fourthyears['Nate'] = 'Georgia Barnes'
print fourthyears # if you assign a value to a key that already exists
                  # the value is changed in place

fourthyears['Terry'] = 'Tom Alber'
print fourthyears #this will update the dictionary with the new key and value
print

