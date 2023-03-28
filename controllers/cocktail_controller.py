from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.cocktail import Cocktail
import repositories.cocktail_repository as cocktail_repository
import repositories.cocktail_ingredient_repository as cocktail_ingredient_repository
import repositories.ingredient_repository as ingredient_repository
import random


cocktails_blueprint = Blueprint('cocktails', __name__)


@cocktails_blueprint.route('/cocktails')
def cocktails():
    ingredient_id = request.args.get('ingredient_id')
    if ingredient_id:
        ingredient = ingredient_repository.select(ingredient_id)
        cocktails = cocktail_repository.select_by_ingredient(ingredient.name)
    else:
        cocktails = cocktail_repository.select_all()
    ingredients = ingredient_repository.select_all()
    return render_template('cocktails/index.html', cocktails=cocktails, ingredients=ingredients)


@cocktails_blueprint.route("/cocktails/<id>", methods=['GET'])
def show_cocktail(id):
    cocktail = cocktail_repository.select(id)

    return render_template('cocktails/show.html', cocktail=cocktail)


@cocktails_blueprint.route("/cocktails/<id>/delete", methods=['POST'])
def delete_cocktail(id):
    cocktail_repository.delete(id)
    return redirect('/cocktails')


@cocktails_blueprint.route('/submit')
def submit_page():
    ingredients = ingredient_repository.select_all()
    return render_template('/submit/index.html', ingredients=ingredients)


@cocktails_blueprint.route('/submit', methods=['POST'])
def add_cocktail():
    name = request.form['cocktail_name']
    description = request.form['cocktail_description']
    instructions = request.form['cocktail_instruction']
    ingredients = request.form.getlist("ingredients")

    new_cocktail = Cocktail(name, description, instructions)
    cocktail_repository.save(new_cocktail)

    for ingredient in ingredients:
        cocktail_ingredient_repository.save(ingredient, new_cocktail.id)
    return redirect('/cocktails')


@cocktails_blueprint.route('/random')
def random_cocktail():
    cocktails = cocktail_repository.select_all()
    random_cocktail = random.choice(cocktails)
    cocktail_ingredients = cocktail_ingredient_repository.select_all_by_cocktail_id(
        random_cocktail.id)
    return render_template('cocktails/random.html', cocktail=random_cocktail, ingredients=cocktail_ingredients)
