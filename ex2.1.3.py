######Tuples
#A tuple is essentially a list that you can not change. 
#You can index, slice them and add them together to make new tuples
#but not use sort(), reverse(), delete or remove items from them. 
#If you ever have a tuple that you want to change, 
#you have to turn it into a list.

trpA = ('protein', 'TIM Barrel')
type(trpA)

for i in trpA:
	print i

#Try to change the tuple by umcommenting below
#trpA[0] = 'RNA'
#print trpA

#:::: TypeError: 'tuple' object does not support item assignment

#change it to a list
trpA = list(trpA)
trpA[0] = 'RNA'
print trpA

