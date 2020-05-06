'''Contains the class to create forms to add recipes including validation'''

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired 

class AddRecipeForm(FlaskForm):
	name = StringField("Recipe: ", validators=[DataRequired()])
	kind = SelectField("Kind: ", choices=[('Soup', 'Soup'), ('Salad','Salad'), ('Meat','Meat'), ('Fish','Fish'),
	 ('Legumes','Legumes'), ('Rice','Rice'), ('Pasta','Pasta'), ('Vegetables/Fruit','Vegetables/Fruit'),
	 ('Bread/Baked','Bread/Baked')], validators=[DataRequired()])
	time = IntegerField("Cooking Time: ", validators=[DataRequired()])
	ingredients = TextAreaField("Ingredients & Quantities: ", validators=[DataRequired()])
	description = TextAreaField("Description: ", validators=[DataRequired()])
	submit = SubmitField("Submit Your Recipe")


