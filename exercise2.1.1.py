#Create a new file. Type in the commands below. 
#Execute the script. Add comments to your script describing 
#what is happening in each line.

L = [1 , 2, 3] + [4, 5, 6] 
#creating a new list, concatenating the two lists using the '+'
 
print L, L[:]  # print the list, no new lines by using a ','
print L[:]     # print the whole list
print L[:0]    # print whole list up to the first digit (an empty list)
print L[-2]    # print the second in the list counting backwards
print L[-2:]   # print the second in the list counting backwards to the
               # until the last one counting forwards
print "-" * 20

L.reverse()    # reverse the list
print L
print "-" * 20

L.sort()       # sort the list least to greatest
print L
print "-" * 20

ind = L.index(4) # tell me where number 4 is in the list
print ind
print "-" * 20

print{'a':1, 'b':2}['b'] #print the value of b in the dictionary containing
                         # the key 'a' with value 1 and 'b' with value '2'
print "-" * 20

D = {'x':1, 'y':2, 'z':3} # initialize a dictionary containing 3 keys, each
                          # with one value
D['w']= 0                 # add the key 'w' to the dictionary with the value 0
print "-" * 20

print D['x'] + D['w']     # print the sum of the values for the keys 'x' and 'w'
                          # the results should be 1

print D.keys()            #print all of the keys in dictionary D
print D.values()          #print all of the values in dictionary D
print D.has_key('z')      #T or F, does dictionary D contain a key called 'z'?
print "-" * 20