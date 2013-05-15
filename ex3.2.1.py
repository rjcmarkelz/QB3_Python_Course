delimiter = ","
string_to_split = "I am a well-written sentence, and so I \
dependably have punctuation. "

list_from_string = string_to_split.split(delimiter)
print "clause one %s" % list_from_string[0]
print "clause two %s" % list_from_string[1]

###
list_from_string = string_to_split.split(' ')
for word in list_from_string:
	print word

list_from_string = string_to_split.split('a')
for vowel_handicapped_lump in list_from_string:
	print vowel_handicapped_lump

list_from_string = list(string_to_split)
for letter in list_from_string:
	print letter

#define how many string splits to do in a row
string_to_split = "I am a well-written sentence, and so I \
 dependably have punctuation. "
list_from_string = string_to_split.split(' ', 3)
for item in list_from_string:
	print item

#two delimitors next to one another
list_from_string = string_to_split.split('t')
for consonant_crippled_lump in list_from_string:
    print consonant_crippled_lump 

print "-"*10
#using defaults this should look the same as the splitting by spaces
list_from_string = string_to_split.split()
for item in list_from_string:
	print item

print "-"*10
#this is not the same as splitting by spaces---no empty items
string_to_split = " this      is   a different               string"
list_from_string = string_to_split.split()
for item in list_from_string:
	print item

print "-"*10
string_to_split = '''    complete
\t\t whitespace                       chaos
                 !!!!!!!!!!!!!!!!!         '''
list_from_string = string_to_split.split()
for item in list_from_string:
	print item

#default split() removes all whitespace at the begining and of the string
#condense all adjacent whitespace to single space characters
#split on those spaces

#however....there are a few hangups using split()
print "-"*10
print "-"*10
print "-"*10
print "stringsplit() hangups:"

toes = '''went to the market
stayed home
had roast beef
had none
cried wee wee wee all the way home'''

#splitlines splits all the linebreaks
list_from_string = toes.splitlines()
for toe in list_from_string:
	print "this little piggy %s" % toe

print "-"*10
#from the end of the string
last_toe = "and_this_little piggy went wee wee wee all the way home"
#when given a second argument, reverse split counts!!!
list_from_string = last_toe.rsplit(' ', 7)
for item in list_from_string:
	print item


print "-"*10
#partition vs. split, similar but different
rhyme = '''There was a crooked man
Who walked a crooked mile.
He found a crooked sixpence
Against a crooked stile.
He bought a crooked cat 
Which caught a crooked mouse, 
And they all lived together
In a crooked little house.'''

#you can split on words as well as single letters and symbols
split_list = rhyme.split('crooked', 1)

print "List output:"
for item in split_list:
	print item

print "-"*10
partition_list = rhyme.partition('crooked')
print "Partition output:"
for item in partition_list:
	print item




#######START HERE#######
####SEARCH ON WEBSITE#####
#What if the delimiter doesn't occur within the string?











