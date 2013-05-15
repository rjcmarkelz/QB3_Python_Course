# You should have a file called '2Q6H.pdb.gz' in your PWD that you 
# downloaded from the PDB. This is a zipped file, which you must unpack to use.
# On a Mac, double click the file to unpack it.
 
# The following block of text is all from 
# http://intro-prog-bioinfo-2009.wikispaces.com/Session2.1
# Initialize list to store sequence:

protSeq = []
file1 = open('2Q6H.pdb', 'r') #open the pdb file, read only allowing the file1
                              #variable to be parsed

for next in file1: # Loop over each line in the file. 'next' could be anything
    if next[:6] =='SEQRES': #identify the lines with sequence
    	line = next.strip().split() #take away white space
    	del line[:4] #delete the descriptor information
    	for aa in line: #loop over the aa's in each line
    		protSeq.append(aa) #add each AA to the list called protSeq
file1.close() #close the file

print '-' * 20
print """We\'ve now read and dissected the file so it\'s in a convenient,
digestible form. The sequence follows:"""
#### Adding occasional print statements helps to know what part of the script
#### is running at any given moment

print
print protSeq
print

#How many total amino acids are in the protein?
print 'There are', len(protSeq), 'amino acids in the protein.'
print

#Print the total count of AAs in alphabetical order
#use set() to turn the list of amino acids in the protein into a set
# of amino acids
setofAAs = set(protSeq)
print setofAAs
print 
print 'The protein contains %s unique amino acids.' % (len(setofAAs))
print


aaDict = { } # make an empty amino acide dictionary

for uniqueAminoAcids in setofAAs:
	aaDict[uniqueAminoAcids] = 0
for aminoacids in protSeq:
	aaDict[aminoacids] = aaDict[aminoacids] + 1



listofAAs = aaDict.keys() #make the list using the keys in the dictionary
listofAAs.sort() #sort the list alphabetically
print "\t", 'aa #', #print headers for columns
print
for alphabeticalAminoAcid in listofAAs:
	print "\t", alphabeticalAminoAcid, aaDict[alphabeticalAminoAcid]
	### Print the AAs along with thier values in the dictionary