''' Main function that will call the necessary functions '''
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#required by 'flash' becasue it works based on cookies
app.secret_key = 'my secret key'

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

#Crate the class for the DB
class Recipes(db.Model):
	__tablename__='recipes'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), unique=True)
	kind = db.Column(db.String(50))
	time = db.Column(db.Integer)
	ingredients = db.Column(db.Text())
	description = db.Column(db.Text())

	def __init__(self, name, kind, time, ingredients, description):
		name = self.name
		kind = self.kind
		time = self.time
		ingredients = self.ingredients
		description = self.description

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
	if request.method == 'POST':
	    
		name = request.form['nameIn']
		kind = request.form['kindIn']
		time = request.form['timeIn']
		ingredients = request.form['ingredientsIn']
		description = request.form['descriptionIn']

		flash('Success! Your recipe has been added.')
		print(name, kind, time, ingredients, description)
		return render_template('index.html')
        

if __name__ == "__main__":
	app.run(debug=True)


