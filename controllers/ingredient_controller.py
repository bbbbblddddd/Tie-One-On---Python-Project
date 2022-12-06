from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.ingredient import Ingredient

import repositories.ingredient_repository as ingredient_repository


ingredients_blueprint = Blueprint('ingredients', __name__)

@ingredients_blueprint.route('/add_ingredient')
def ingredients():
    ingredients = ingredient_repository.select_all()
    return render_template('add_ingredient.html', ingredients = ingredients)


@ingredients_blueprint.route('/add_ingredient', methods = ['POST'])
def add_ingredient():
    name = request.form['ingredient_name']
    new_ingredient = Ingredient(name)
    ingredient_repository.save(new_ingredient)
    return redirect('/add_ingredient')



