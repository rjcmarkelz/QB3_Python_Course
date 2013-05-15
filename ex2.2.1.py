#if statment

checkingacountbalance = 4

if checkingacountbalance < 10:
	thisweeksfood = 'ramen'
if checkingacountbalance >= 10:
	thisweeksfood = 'goodramen'
print "We are eating %s this week" % (thisweeksfood)

if checkingacountbalance == 15:
	thisweeksfood = 'that particular brand of good ramen'

if checkingacountbalance != 15:
	thisweeksfood = 'certainly not that brand!'

	print 'absolutely not!'

print "-" * 20
print 


#if and else
if checkingacountbalance < 10:
	thisweeksfood = 'ramen'
else:
	thisweeksfood = 'goodramen'

#if, elif and else that help account for all posibilities
if checkingacountbalance < 10:
	thisweeksfood = 'ramen'
elif checkingacountbalance < 100:
	thisweeksfood = 'good ramen'
elif checkingacountbalance < 200:
	thisweeksfood = 'better ramen'
else:
	thisweeksfood = 'ramen that is truley profound in its goodness'

print "-" * 20 
print


