#functions

#define the functions
#def to define the function
#then give it a name, in this case hello
#parenthesis are input arguments, in this case name
#return that greeting to the rest of the program
#technically you do not need to return anything, but 
#   python will return None anyway as a logically FALSE statement
def hello(name):
	greeting = "Hello %s!" % (name)
	return greeting

#use the fucntion
functionInput = 'Zaphod Beeblebrox'
functionOutput = hello(functionInput)
print functionOutput

print "---"*10

#showing that variable names within functions maintain thier own 
#namespace in memory, see folling web link for more info
#http://bytebaker.com/2008/07/30/python-namespaces/
def hello(name):
	greeting = "Hello %s!" % (name)
	testVariable = """ The hotel room is a mess
	                   b;ah blah blah I do not feel like typing"""
	print 'Inside of the function:', testVariable
	return greeting

testVariable = "What happens in Vegas stays in Vegas."
grt = hello("Stu Price")
print 'Outside of the function:', testVariable

print "---"*10

#here is a much more complicated function with many options 
# in the 
def whichFood(balance):
	if balance < 10:
		return 'raman'
	elif balance < 100:
		return 'good ramen'
	elif balance < 200:
		return 'better ramen'
	else:
		return 'ramen that is truly profound in its goodness'
print whichFood(14)

print "---"*10

#functions can work without input/output
#here are a few examples:
def useless():
	print 'What?'
	print

useless()

def countToTen():
	for i in range(10):
		print i

countToTen()
print "---"*10

#multiple items in, multiple items out example of function
#this returns a tuple, but one could also return a list or dictionary
def doLaundry(amtDetergent, dirtyClothes):
    cleanClothes = []
    for load in dirtyClothes:
    	amtDetergent -= 1
    	cleanClothes.append(load)
    return (amtDetergent, cleanClothes)

amtTide = 5
dirtyLaundry = ['socks', 'shirts', 'pants']
(amtTide, cleanLaundry) = doLaundry(amtTide, dirtyLaundry)
print "Amount of Tide Left:", amtTide
print cleanLaundry

print 
print "---"*10
print

def returnStuff():
	a = '>Gene1'
	b = 'ATGGTGGG'
	return [a,b] # returns the output as a list

print type(returnStuff())

#index the list output to a list
print returnStuff()[0]
print returnStuff()[1]

(name, seq) = returnStuff() # stores output to the variables x & y,
                            # so you can access x and y directly
print 
print
print name
print seq
print 
print

print "into a list:"
both = returnStuff() #stores output to the variable both
                     # which will be in a list
print both

print
print "into a dictionary:"
dictOfStuff = {}
dictOfStuff[returnStuff()[0][1:]] = returnStuff()[1]
print dictOfStuff

print 
print "---"*10
print
#programs make mundane tasks easier, with less likelyhood for human
#error

def publishAPaper(authors, topic, journal):
	data = doWork(topic)
	figures = analyze(data)
	paper = writePaper(data, figures)
	aubmit(authors, paper, journal)

print "Hurray! We have the outline of a paper generator function!"
print
print

#################
#start at modules
#################



