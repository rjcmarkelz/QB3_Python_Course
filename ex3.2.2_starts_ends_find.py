#!/usr/bin/env python

id_number = '1131431a'

#id start with 1?
if (id_number[0] == '1'):
	print "this id starts with a 1!"

if ( id_number.startswith('1') ):
	print "startswith: this id starts with a 1!"

if ( id_number.endswith('1') ):
	print "this id ends with a 1"
else:
	print "this id does not end with a 1!"

#try adding a tuple to search for multiple things
if id_number.endswith( ('1', 'a') ):
	print "this id number ends with either an 'a' or a '1' "
else:
	pass



beatles = "johnpaulgeorgeandringo"
#be careful when using an if statement with find
#it finds the indexed number
if ( beatles.find('paul')):
	print "At least we've got a bassist."
else:
	print "Anyone here play bass?"

if not (beatles.find('paul') == -1):
	print "At least we've got a bassest."
else:
	print "Well, I guess we're a three piece."

#text conversions
beatles = "johnpaulgeorgeandringo"
beatles = beatles.replace('george', 'JUSTIN')
print beatles

beatles = beatles + "MOREJUSTIN!"
print beatles.replace("JUSTIN", "DIANNA!")
print beatles

#you can also tell where to replace
print beatles.replace("JUSTIN", "DIANNA!", 1)
print beatles

#replace does not change the string in place
#if you want this new assignment to stay then a new variable needs
# to be assigned


#playing with string cases
blast_hit = 'ATATATATATGGGCTCTCTATCGCTCGaaaatttgggtttcccAATTTAAAA'

#upper
if (blast_hit.isupper()):
	pass
else:
	blast_hit = blast_hit.upper()
	print blast_hit

#lower
blast_hit = blast_hit.lower()
print blast_hit

#swapcase
blast_hit =blast_hit.swapcase()
print blast_hit

#or to make sure there are only letters
if (blast_hit.isalpha()):
	print "we have all letters here"
else:
	print "something is up with our sequence data"


















