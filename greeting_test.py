#!/usr/bin/env python

import greeting_module

hi = greeting_module.hello('Peter')
print hi
print greeting_module.x

import sys
print greeting_module.hello(sys.argv[1])
#take terminal argument as input from the greeting


#if you wanted ONLY the ahoy part uncomment below
from greeting_module import ahoy
hi = ahoy('everybody')
#print hi

#note that if you grab a single function from a module, 
#the module.function syntax

#or to import a function of a module as something...
from greeting_module import ahoy_hoy, hello

#or
from greeting_module import * #wildcard character

hi = ahoy('everybody')
hi2 = hello('everybody')

#one last trick
import greeting_module as gm

#can add this to your bash profile for modules that get used all of the time
# $ echo 'PYTHONPATH=~/Library/Python/Modules' >> .bash_profile
# $ echo 'export PYTHONPATH' >> .bash_profile
# $ source .bash_profile