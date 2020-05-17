''' Will have the functiosn to generate the randoms recipe '''
### Rename file as 'retrieve.py'
import random

def getRandomIndex(upperlimit): 
	''' Generates a random integer between 0 and the entered upper limit.
	    This integer will be used as an index for 'recipes_from_db' list'''

	print("\n **UPPERLIMIT: ", upperlimit)
	#return random.randint(0, upperlimit)


def selectRecipes(numrecipes, recipelist):
	'''  	
	finallist = []
	#range() determins how many times we randomly select a recipe
	for i in range(numrecipes):
		#Randomly selects a recipe form the ones collected from DB
		idx = getRandomIndex(len(recipelist)-1)
		finallist.append(recipelist[idx])
	return finallist
	'''
	pass