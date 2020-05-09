'''Contains the class to create forms to add recipes including validation'''

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, BooleanField, RadioField, Form
from wtforms.validators import DataRequired 

class AddRecipeForm(FlaskForm):
	name =        StringField("Recipe: ", validators=[DataRequired()])
	kind =        SelectField("Kind: ", choices=[('Soup', 'Soup'), ('Salad','Salad'), ('Meat','Meat'), ('Fish','Fish'),
	              ('Legumes','Legumes'), ('Rice','Rice'), ('Pasta','Pasta'), ('Vegetables/Fruit','Vegetables/Fruit'),
	              ('Bread/Baked','Bread/Baked')], validators=[DataRequired()])
	time =        IntegerField("Cooking Time: ", validators=[DataRequired()])
	ingredients = TextAreaField("Ingredients & Quantities: ", validators=[DataRequired()])
	description = TextAreaField("Description: ", validators=[DataRequired()])
	
	submit = SubmitField("Submit Your Recipe")


class GetRecipeForm(FlaskForm):
	all =        BooleanField("All", default="checked")
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
				 ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], validators=[DataRequired()])

	submit = SubmitField("Get Your Recipe")
