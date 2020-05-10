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
	#Validate_on_submit already takes into account if the method is POST
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
		'''
		kind_recipes = request.args.getlist('kindRecipes')
		num_recipes = request.args.get('numRecipes')

		print('kind recipes: ', kind_recipes)
		print('num_recipes: ', num_recipes)
		'''

		get_form = GetRecipeForm(request.args)
		'''
		checklist = request.args.getlist("kindRecipes")
		print("Checklist: ", checklist)
		'''
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
		#create a list of the 
		sr =list( map(lambda x: x[0], list( filter( lambda elem: elem[1], selected_recipes.items() ))))
		
		print( "SR: ", sr)
		print("selected_number:", selected_number)


		'''
		#1. Extract all recipes that are of kind_recipes
		rcps = []
		for kind in kind_recipes:
			rcps += db.session.query(Recipe).filter(Recipe.kind == kind).all()

		#2. Put them in a list of tuples where first element of each tuple is a number
		matching_recipes = list(enumerate(rcps))
		print('kind recipes: ', kind_recipes)
		print('rcps: ', rcps)
		print('matching_recipes: ', matching_recipes)

		
		#3. Loop: (runs as many times as num_recipes)
		#3.1.Generate an integer from 1 to the total number of recipes in the dic
		num_list = []
		for i in range(num_recipes):
			num_list.append(random_key(len(matching_recipes)))
		#3.2.Select from the dict the recipe whose key is that number
		#filter(, matching_recipes)
		#3.3.Displays the recipe in index.html OR create list holding all recipes and then
		#    we loop through them to display them
	
		'''
		#return render_template('index.html', add_form=add_form, kind_recipes=kind_recipes, num_recipes=num_recipes)
		return render_template('index.html', add_form=add_form, get_form=get_form)
	
	#In case the POST submition didn't go well
	#return render_template('index.html', add_form=add_form, kind_recipes=kind_recipes, num_recipes=num_recipes)
	return render_template('index.html', add_form=add_form, get_form=get_form)

if __name__ == "__main__":
	app.run()


