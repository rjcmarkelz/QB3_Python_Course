### getting to know your TA's

listTAs = ['Debbie', 'Justin', 'Mel', 'Ben']
print listTAs
print

#what happens if you index out of range?
print listTAs[3] # this would be in range
#print listTAs[10] # this would be out of range with an error
print

#Slice out of bounds
print listTAs[3:5] # in bounds
print listTAs[3:14] # out of bounds, but would return the 
                    #list of inbounds values

print listTAs[30:40] # return an empty listTAs

#slice in reverse?
print listTAs[5:3] #returns empty list

print listTAs
listTAs[2:2] = ['Cody']
print listTAs
listTAs.insert(4, 'Sharon')
print listTAs
print

listTAs[3:5] = ['what does this do?'] #adds 'what does this do' to positions
                                      #3 and 4
listTAs[5:2] = ['uh...?'] # adds 'uhh' to index 5
print listTAs

print 