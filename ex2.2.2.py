# logic operators combined with if else statements
s = 0 

if s:
	print "s is True!"
else:
	print "s is False!"

if s == 0:
	print "s is True!"
else: 
	print "s is False!"

print "-" * 20

# logic boolean
true_statement = 'truth itself' #non-empty strings are true_statement
false_statement = '' # empty strings are false

if true_statement and false_statement:
	print "This should not print."
else:
	print "This should print."

if true_statement or false_statement:
	print "This should print."

if not false_statement:
	print "This should print."

if not (true_statement and false_statement):
	print "This should print."

print "-" * 20

# for loops
list1 = ['Red Leicester', 'Gruyere', 'Camembert', 'Permesan', 'Mozarella',
              'Chedder']

for x in list1:
	print x
print "-" * 20


# for loops
list2 = ['Red Leicester', 'Gruyere', 'Camembert', 'Permesan', 'Mozarella',
              'Chedder']

for x in list2:
	print "Cleese: Do you have any %s?" % x
	if x == 'Camembert':
		print "Chapman: Ohh, the cat's eaten it!"
	else:
		print "Chapman: No."
print "Cleese: Well I'm sorry, but I'm going to have to shoot you."

print "-" * 20

#Looping a given number of times
for x in range(4):
	print 'hello'

y = range(4)
print y

print "-" * 20

# mutating lists
#this will not work
#see mutables.py
list3 = [1, 22, 48, 36, 101]
print list3

for x in list3:
	x = x + 42
print list3

print "-" * 20

#now we can replace the values
list2 = [1, 22, 48, 36, 101, 42]
print list2

for x in range(len(list2)):
	list2[x] = list2[x] + 23
print list2
print '-' * 20

#python has a built in function for things like this enumerate()

print list2
for xind, x in enumerate(list2):
	print x
	list2[xind] = list2[xind] + 23
	print x
	print

print list2
print '-' * 20 

#while loops
x = 'Here we go again!'
while x:
	print x
	x = x[1:]
print

x = 5
while x > 0:
	print x
	x = x - 1
print '-' * 20 

#escaping loops
#while True:
#	dividend = int(raw_input("Dividend: "))
#	divisor = int(raw_input("Divisor: "))
#	if divisor == 0:
#	print dividend/divisor

print "-" * 20

# escaping loops example 2
x = 10 
while x:
	x = x - 1
	if x % 2 == 0:
		continue
	print x,
print "-" * 20

#escaping loops example 3
y = 10
x = y - 1
while x >1:
	if y % x == 0:
		print x, "is a factor of", y
		break
	x = x - 1
else:
	print y, 'is prime'

# List comprehensions
a = range(10)
b = []
for i in a:
	b.append(i + 1)
a = b
print a


a = range(10)
print [ i + 1 for i in a ]
a = [ i + 1 for i in a ]
print a


































