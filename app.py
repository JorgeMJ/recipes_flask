''' Main function that will call the necessary functions '''
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from recipeForms import AddRecipeForm, GetRecipeForm


app = Flask(__name__)

app.debug=True
#required by 'flash' becasue it works based on cookies
#app.secret_key = 'my secret key'
app.config['SECRET_KEY'] = 'my secret key'

#Variable ENV determines the environment
ENV = 'dev'

#Set the environment
if ENV == 'dev':
	app.debug = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/random_recipes'
else:
	app.config['SQLALCHEMY_DATABASE_URI'] =''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Create the database object
db = SQLAlchemy(app)

#Crate the table for the DB
class Recipe(db.Model):
	__tablename__='recipes'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), unique=True)
	kind = db.Column(db.String(50))
	time = db.Column(db.Integer)
	ingredients = db.Column(db.Text())
	description = db.Column(db.Text())

	def __init__(self, name, kind, time, ingredients, description):
		self.name = name
		self.kind = kind 
		self.time = time
		self.ingredients = ingredients
		self.description = description


@app.route('/', methods=['POST', 'GET'])
def submit():
	add_form = AddRecipeForm()
	get_form = GetRecipeForm(request.args)
	
	if add_form.validate_on_submit():	
		#Takes the input data from form
		name = add_form.name.data
		kind = add_form.kind.data
		time = add_form.time.data
		ingredients = add_form.ingredients.data
		description = add_form.description.data

		'''
		if db.session.query(Recipe).filter(Recipe.name == name).count() == 1:
			flash("That recipe already exists. Provide a different recipe.", "warning")
			return render_template('index.html')
		'''
		'''
		##**Add a 'try-catch' block if the submition throws an error. It catches an error flash 'an error ocurred'**
		##**if not, flash 'success' and finally, redirect (either case)
		'''
		#Add new recipe to the DB
		new_recipe = Recipe(name, kind, time, ingredients, description)
		db.session.add(new_recipe)
		db.session.commit()

		flash('Success! Your recipe has been added.', 'success')
		return redirect(url_for('submit')) 

	elif request.method == 'GET':
		
		selected_recipes = {
			'All': get_form.all.data,
			'Soup': get_form.soup.data,
			'Salad': get_form.salad.data,
			'Meat': get_form.meat.data,
			'Fish': get_form.fish.data,
			'Legumes': get_form.legumes.data,
			'Rice': get_form.rice.data,
			'Pasta': get_form.pasta.data,
			'Vegetables': get_form.vegetables.data,
			'Dessert': get_form.dessert.data,
			'Bread': get_form.bread.data
		}
		selected_number = get_form.number.data

		#create a list of selected recipes
		selected_recipes_list = list( map(lambda elem: elem[0], list( filter( lambda elem: elem[1], selected_recipes.items() ))))
		
		#Selects from the DB the recipes of the selected kinds
		match_recipes = []
		for item in selected_recipes_list:
			for elem in db.session.query(Recipe).filter(Recipe.kind == item).all():
				match_recipes.append(elem)

			#1.1. if the total number of recipes is less than the selected_number, flash and redirect.
		
		#2. Put recipes in a list of tuples where first element of each tuple is a number
		numbered_match_recipes = list(enumerate(match_recipes))
		'''
		#3. Create a function that accepts 'selected_number' and 'matching_recipes' list of touples.
			3.1. this function has a for loop that runs 'selected_number' of times.
			     Each time it runs the random_integer (limits 1:length of 'matching_recipes')
			     the chosen recipes as store in a list that is returned

		#4. Function that displays (renders??) the list or recipes in HTML:
			4.1. for loop to go through each element of the list
			4.2. the elements containg the recipes, has a toggle js funtion to show/hide each. 
	
		'''
		#return render_template('index.html', add_form=add_form, kind_recipes=kind_recipes, num_recipes=num_recipes)
		return render_template('index.html', add_form=add_form, get_form=get_form)
	
	#In case the POST submition didn't go well
	#return render_template('index.html', add_form=add_form, kind_recipes=kind_recipes, num_recipes=num_recipes)
	return render_template('index.html', add_form=add_form, get_form=get_form)

if __name__ == "__main__":
	app.run()


