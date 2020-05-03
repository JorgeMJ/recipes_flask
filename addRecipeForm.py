'''Create forms to add recipes including validation'''

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import InputRequired #DataRequired

class AddRecipeForm(FlaskForm):
	name = StringField("Recipe: ", validators=[InputRequired()])
	kind = SelectField("Kind: ", choices=['Soup', 'Salad', 'Meat', 'Fish', 'Legumes', 'Rice', 'Pasta', 'Vegetables/Fruit', 'Bread/Baked'], validators=[InputRequired()])
	time = IntegerField("Cooking Time: ", validators=[InputRequired()])
	ingredients = TextAreaField("Ingredients: ", validators=[InputRequired()])
	description = TextAreaField("Description: ", validators=[InputRequired()])
	submit = SubmitField("Submit Your Recipe")


