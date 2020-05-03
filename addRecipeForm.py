'''Create forms to add recipes including validation'''

from Flask import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import InputRequired #DataRequired

class AddRecipeForm(FlaskForm):
	name = StringField("Recipe: ", validator=[InputRequired()])
	kind = SelectField("Kind: ", choices=['Soup', 'Salad', 'Meat', 'Fish', 'Legumes', 'Rice', 'Pasta', 'Vegetables/Fruit', 'Bread/Baked'], validator=[InputRequired()])
	time = IntegerField("Cooking Time: ", validator=[InputRequired()])
	ingredients = TextAreaField("Ingredients: ", validator=[InputRequired()])
	description = TextAreaField("Description: ", validator=[InputRequired()])
	submit = SubmitField("Submit Your Recipe")