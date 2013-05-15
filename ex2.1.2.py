#shrinking a list
list1 = ['Why', 'do', 'superheroes', 'wear', 'spandex']
print list1
print

#remove an item from the list
#1) The built-in function del removes a particular item from the list.
print list1
del list1[3]
print list1
print

#remove the last item using pop
#2) The list method pop() removes the last item from the list and 
#returns the variable.
word = list1.pop()
print list1
print word
print

#remove the last item from the list by slicing
#The last way, removal by slicing, is essentially redefining the 
#list to be everything except the last item of the original list.
list1 = list1[:-1]
print list1

###########
###########
###########
# Changing lists in place
#create a list of zeros

nolist = 4 * [0]
print nolist
print

#modify items in the nolist
mice_brain  = 10
rat_brain   = 20
human_brain = 500

#1) Overwritten items in the list using slices.
nolist[2]   = mice_brain
nolist[1]   = rat_brain
nolist[3]   = human_brain

print nolist
print

#sort list
#2) Sorted the list using the method sort() and the function sorted(). 
#sort() works on the list in place, while sorted() returns a new list.

nolist.sort()
print nolist

# sorting into a new list
another_nolist = sorted(nolist)
print another_nolist
print

#reverse order
#3) Reversed the order of the list using the method reverse().

nolist.reverse()
print nolist
print

# sort string list
print list1
list1.sort()
print list1
list1.reverse()
print list1

###########
###########
###########
#Charaterizing lists

#figure out how long the lists are 
#1) The built-in functions len(), max() and min() 
#tell us how many items are in the list and the maximum and 
#minimum values in the list.
print list1
print len(list1)
print nolist
print len(nolist)
print 'Max = ', max(nolist)
print 'Min = ', min(nolist)
print

#iterate over the list
#3) We can iterate over each item in the list and print it using 
#the syntax for x in [ ]:
for x in list1:
	print x
print

#find where something is 
#2) The list method index() tells us where an item is in the list.
idx_list1 = list1.index('Why')
print idx_list1
print





































