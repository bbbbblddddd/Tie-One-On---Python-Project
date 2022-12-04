from flask import Flask, render_template

# from controllers.
# from controllers.
# from controllers.

app = Flask(__name__)

# app.register_blueprint(cocktails_blueprint)
# app.register_blueprint(ingredients_blueprint)
# app.register_blueprint(cocktail_ingredient_blueprint)
# app.register_blueprint(cocktail_quantity_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)