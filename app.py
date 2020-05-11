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
		#Add new recipe to the DB
		new_recipe = Recipe(name, kind, time, ingredients, description)
		db.session.add(new_recipe)
		db.session.commit()

		flash('Success! Your recipe has been added.', 'success')
		return redirect(url_for('submit')) 

	elif request.method == 'GET':
		
		selected_recipes = {
			'all': get_form.all.data,
			'soup': get_form.soup.data,
			'salad': get_form.salad.data,
			'meat': get_form.meat.data,
			'fish': get_form.fish.data,
			'legumes': get_form.legumes.data,
			'rice': get_form.rice.data,
			'pasta': get_form.pasta.data,
			'vegetables': get_form.vegetables.data,
			'dessert': get_form.dessert.data,
			'bread': get_form.bread.data
		}
		selected_number = get_form.number.data

		#create a list of selected recipes
		selected_recipes_list = list( map(lambda elem: elem[0], list( filter( lambda elem: elem[1], selected_recipes.items() ))))
		

		'''
		this flash shows on load. How to fix it??
		if len(selected_recipes_list) == 0:
			flash("You must select a recipe kind.", "warning")
		else:
			pass

		#1. Extract all recipes that are of kind_recipes
		rcps = []
		for kind in kind_recipes:
			rcps += db.session.query(Recipe).filter(Recipe.kind == kind).all()

			1.1. if the total number of recipes is less than the selected_number, flash and redirect.

		#2. Put recipes in a list of tuples where first element of each tuple is a number
		matching_recipes = list(enumerate(rcps))
		
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


