''' Main function that will call the necessary functions '''
from flask import Flask, render_template, request, flash


app = Flask(__name__)
#required by 'flash' becasue it works based on cookies
app.secret_key = 'my secret key'

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
    app.debug = True
    app.run(debug=True)


