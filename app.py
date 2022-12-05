from flask import Flask, render_template

from controllers.cocktail_controller import cocktails_blueprint
from controllers.ingredient_controller import ingredients_blueprint

from repositories import ingredient_repository


app = Flask(__name__)

app.register_blueprint(cocktails_blueprint)
app.register_blueprint(ingredients_blueprint)

@app.route('/')
def home():
    ingredients = ingredient_repository.select_all()
    return render_template('index.html', ingredients = ingredients)

if __name__ == '__main__':
    app.run(debug=True)