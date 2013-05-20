#!/usr/bin/env python

#basic structure
# fh = open('hello.py')
# contents = fh.read()
# print contents
# fh.close()


#example with out strip
filename = 'pdb_head'
fh = open(filename, 'r')

print fh.readline()
print fh.readline()

lines = fh.readlines()

fh.close()

print lines
print "-"*10

# fh.readline() takes in one line (and since print() also supplies a newline, 
	#we've got an extra linebreak after each of the first two print statements.
# fh.readlines() (plural!) takes the entire file, from the current read 
    #position all the way to the end, giving back a list of lines (again, 
    #with newlines intact).
# This file has a bunch of whitespace cluttering things up at 
    #the end of each line.

filename = 'pdb_head'
fh = open(filename, 'r') #read file

print fh.readline().strip()
print fh.readline().strip()

lines = fh.readlines()


fh.close()

lines[0] = lines[0].strip()

print lines
print "-"*10
print "-"*10
#####IMPORTANT##### Each time a line is read into Python it advances the 
#position in the filehandle by 1 so that it can be incremented
#this is refered to as iterable type


#reading files in a loop
fh = open('pdb_head')
lines = fh.readlines()
for line in lines:
	fields = []
	fields.append(line[0:6].strip())
	fields.append(line[6:10].strip())
	print "0th field: %s, 1st field: %s " %(fields[0], fields[1])
fh.close()
#the ouput makes sense, but filehandle are already iterable!!!
print "-"*10
print "-"*10

#reading files in a loop
fh = open('pdb_head')
for line in fh:
	fields = []
	fields.append(line[0:6].strip())
	fields.append(line[6:10].strip())
	print "0th field: %s, 1st field: %s " %(fields[0], fields[1])
fh.close()
print "-"*10
print "-"*10

filename = 'test_out'
fh = open(filename, 'w') #write to file

fh.write('Historically, this lesson was used as a medium to hurtle insults')
fh.write('Matt and our former labmate \n')

fh.close()

filename = 'test_out2'
fh = open(filename, 'a') #append to file

fh.write("blah blah blah")

fh.close()

print "-"*10
print "-"*10


filename = 'test_out3'
fh = open(filename, 'w')

lines = ["Justin is a friendly dude. \n, You'd better be one too.\n"]
lines.extend(["or next year, he might ust this space\n",
	          "to write phish songs about you.\n "])

fh.writelines(lines)
fh.close()











