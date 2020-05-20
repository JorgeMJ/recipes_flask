''' Contains the functions to randomly select recipes from the recipe list created from the DB. '''

import random

def getRandomIndex(upperlimit): 
	''' Generates a random integer between 0 and the entered upper limit.
	    This integer will be used as an index for 'recipes_from_db' list'''
	return random.randint(0, upperlimit)
	

def selectRecipes(numrecipes, recipelist):
	''' Returns a list containing randomly selected items from an input list. '''
	finallist = []	
	while len(finallist) < numrecipes:
		#Randomly selects a recipe form the ones collected from DB.
		idx = getRandomIndex(len(recipelist)-1)
		if recipelist[idx] not in finallist:
			finallist.append(recipelist[idx])
	return finallist
