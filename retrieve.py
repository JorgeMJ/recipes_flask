''' Will have the functiosn to generate the randoms recipe '''
### Rename file as 'retrieve.py'
import random

def random_key(upper_limit): 
	''' Generates a random integer between 1 and the entered upper limit.
	    This number will be used as a matching key for the dictionary '''
	return random.randint(1, upper_limit)

