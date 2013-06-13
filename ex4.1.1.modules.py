import sys
import math

# commandLine = sys.argv
# print commandLine

# x = float(sys.argv[1])

# logX = math.log(x)
# print logX

#######
#Collections
#######
import collections

my_genera = ['Helicobacter', 'Escherichia', 'Lactobacillus', 'Lactobacillus', 'Oryza',
             'Wolbachia', 'Oryza', 'Rattus', 'Lactobacillus', 'Drosophila']

c = collections.Counter(my_genera)
print c

d = collections.Counter()

for genus in my_genera:
	d[genus] += 1

print d

print c.most_common()

print "-" * 20

###with dictionary
###not as straight forward
e = {}

for genus in my_genera:
	if genus not in e:
		e[genus] = 0
	e[genus] += 1

print "-" * 20
print "-" * 20

###default dictionary option
my_species_list = [('Helicobacter','pylori'), ('Escherichia','coli'),
              ('Lactobacillus', 'helveticus'), ('Lactobacillus', 'acidophilus'),
              ('Oryza', 'sativa'), ('Wolbachia', 'pipientis'), ('Oryza', 'glabberima'),
              ('Rattus', 'norvegicus'), ('Lactobacillus','casei'),
              ('Drosophila','melanogaster')]
d2 = {}

for genus, species in my_species_list:
	if genus not in d2:
		d2[genus] = []
	d2[genus].append(species)

print d2
print "-" * 20

d3 = collections.defaultdict(list)

for genus, species in my_species_list:
	d3[genus].append(list)

print d3
print "-" * 20

####Making a module####












