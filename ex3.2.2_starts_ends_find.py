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


####START AT BEATLES EXAMPLE#####
#beatles = "johnpaulgeorgeandringo"
 