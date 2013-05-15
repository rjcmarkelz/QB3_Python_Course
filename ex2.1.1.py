#Lists

list1 = ['duck', 'season']
list2 = ['wabbit', 'season']
list3 = ['...Fire!']

#print Lists
print list1
print list2
print list3
print

#access single items from lists 
print list1[0], list2[0], list3[0]
print list1[:]
print

#add a single item to the end of list1
#1) The list method append(), which adds a single item to the end of a list
list1.append(list2[0])
print list1
print

list1.append(list2[1])
print list1
print

#combine two lists by extension
#2) The list method extend(), 
#which adds a whole list to the end of the list you ask to extend itself
print list1
list1.extend(list2)
print list2
print list1
print


#combine two lists by concatenation
#3) The list concatenation operator, which 
#stitches two things together to make a new whole, without changing either original list.
list4 = list1 + list3
print list1
print list3
print list4
print

#print out slices of list
print list4
print list4[2:]
print list4[:4]
print list4[1:3]
print list4[-1:]
print list4[-2:]
print list4[:-1]
print list4[1:4:2]
print list4[::-1]

print