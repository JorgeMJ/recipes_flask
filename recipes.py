''' Main function that will call the necessary functions '''
from flask import Flask, render_template, request


app = Flask(__name__)

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
       
        print(name, kind, time, ingredients, description)
        return('Success')
        



if __name__ == "__main__":
    app.debug = True
    app.run()


