--- TABLE OF CONTENTS ---

	.RANDOM_RECIPES
	.FILE STRUCTURE
	.FILES
	.RUNNING
	.CONTACT

RANDOM_RECIPES:

Random_Recipe_Selector is a Flask app that allows users to obtain recipes from the database in a random fashion but following the restrictions the user chooses: Number of recipes to be displayed and kind of recipes. The user can also add recipes to the database that will become part of the recipe pool from which the program select recipes randomly.

You can try the Random_Recipe_Selector here: https://young-lowlands-24109.herokuapp.com/

FILE STRUCTURE:

	{Root}
	 |
	 +----{static}
	 |     |
	 |     +----style.css
	 |     |
	 |     +----style.js
	 |     |
	 |     +----script.js
	 |
	 +----{templates}
	 |     |
     |     +----index.html
     |     |
     |     +----recipeList.html
     |     |
     |     +----messages.html
     |
     +----app.py
     |
     +----recipeForms.py
     |
     +----retrieve.py
     |
     +----Pipfile
     |
     +----Pipfile.lock
     |
     +----requirements.txt
     |
     +----.gitignore
     |
     +----Procfile
     |
     +----runtime.txt
     |
     +----README.md


FILES:

<ul>
	<li>style.css : Style of the page.</li>
	<li>style.js : JavaScript functions for styling the app.</li>
	<li>script.js : contain the function to check the checkbox 'All' when index.html loads.</li>
	<li>index.html : Main page.</li>
	<li>recipeList.html : displays the list of recipes retrieved form the database.</li>
	<li>messages.html : Show messages of success, error, and warnings.</li>
	<li>app.py : The app itself. Establishes the database, table, server, forms.</li>
	<li>recipeForms.py : Contains the classes to build the forms.</li>
	<li>retrieve.py : Contains the functions to randomly retrieve recipes.</li>
	<li>.gitignore : Lists of files Git should ignore.</li>
	<li>Pipfile : Specifies the packages requirements.</li>
	<li>Pipfile.lock : Specifies the version of the required packages.</li>
	<li>Procfile : Declares how the app must be run (uses gunicorn to deploy in heroku).</li>
	<li>requirements.txt : Specifies the dependencies needed.</li>
	<li>runtime.txt : Specifies what Python version is needed.</li>
</ul>

**NOTE: WTForms package seems to have a bug that doesn't allow the attribute 'default=checked' for BooleanField to work. To walk around this issue, I wrote a function in 'script.js' that checks the checkbox 'All' for 'Get Recipe Form' if no other checkbox has been previously checked in redirection.

RUNNING:

To run it locally in development mode, you have to change in 'app.py' the variable ENV = 'prod' to ENV = 'dev'

After setting the database, it is necessary to create the table 'feedback' that will hold all the information the user introduces. To do that, you have to open the Python interpreter and run the following:

from app import db

db.create_all()

exit()

CONTACT:

Author: Jorge Martin Joven; Email: jmartinjoven@gmail.com; Github: https://github.com/JorgeMJ

