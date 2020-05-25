'''Contains the classes to create 'Add Recipe Form' and 'Get Recipe Form' including validation'''

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, BooleanField, RadioField, Form
from wtforms.validators import DataRequired 

class AddRecipeForm(FlaskForm):
	''' Defines an AddRecipeForm object.'''
	name =        StringField("Recipe: ", validators=[DataRequired()])
	kind =        SelectField("Kind: ", choices=[('Soup', 'Soup'), ('Salad','Salad'), ('Meat','Meat'), ('Fish','Fish'),
	              ('Legumes','Legumes'), ('Rice','Rice'), ('Pasta','Pasta'), ('Vegetables/Fruit','Vegetables/Fruit'),
	              ('Bread/Baked','Bread/Baked')], validators=[DataRequired()])
	time =        IntegerField("Cooking Time: ", validators=[DataRequired()])
	ingredients = TextAreaField("Ingredients & Quantities: ", validators=[DataRequired()])
	description = TextAreaField("Description: ", validators=[DataRequired()])
	
	submit = SubmitField("Submit Your Recipe")

	def __repr__(self):
		''' Returns an object representation of the class. '''
		return '{self.__class__.__name__}'.format(self=self)



class GetRecipeForm(Form):
	''' Define a GetRecipeForm object. '''
	all =        BooleanField('All')
	soup =       BooleanField('Soup')
	salad =      BooleanField('Salad')
	meat =       BooleanField('Meat')
	fish =       BooleanField('Fish')
	legumes =    BooleanField('Legumes')
	rice =       BooleanField('Rice')
	pasta =      BooleanField('Pasta')
	vegetables = BooleanField('Vegetables/Fruit')
	dessert =    BooleanField('Desserts')
	bread =      BooleanField('Bread/Baked')
	number =     RadioField("Number of Recipes:", choices=[('1', '1'), ('2', '2'), ('3', '3'),
				 ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], default='1')

	submit = SubmitField("Get Your Recipe")

	def __repr__(self):
		''' Returns an object representation of the class. '''
		return '{self.__class__.__name__}'.format(self=self)
