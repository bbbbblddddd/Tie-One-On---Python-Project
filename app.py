from flask import Flask, render_template

from controllers.cocktail_controller import cocktails_blueprint
from controllers.ingredient_controller import ingredients_blueprint


app = Flask(__name__)

app.register_blueprint(cocktails_blueprint)
app.register_blueprint(ingredients_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)