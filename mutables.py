a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
a[0] = 'X'

print a

b = a 
print b

b[1] = 'Y'
print b, "is a value of b"
print a, "is a value of a"
print '-' * 20




c = 'abcdef'

d = c

c = 'asdfasdf'
#notice that c has been reassigned to 'asdfasdf'
# but d still points to the same values in
# the original c 'abcdef'
print c
print d



