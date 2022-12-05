from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.cocktail import Cocktail
import repositories.cocktail_repository as cocktail_repository
import repositories.cocktail_ingredient_repository as cocktail_ingredient_repository



cocktails_blueprint = Blueprint('cocktails', __name__)

@cocktails_blueprint.route('/cocktails')
def cocktails():
    cocktails = cocktail_repository.select_all()
    return render_template('cocktails/index.html', cocktails = cocktails)

@cocktails_blueprint.route("/cocktails/<id>", methods=['GET'])
def show_cocktail(id):
    cocktail = cocktail_repository.select(id)
    
    return render_template('cocktails/show.html', cocktail = cocktail)

@cocktails_blueprint.route('/cocktails<id>/delete', methods=['POST'])
def delete_cocktail(id):
    cocktail_repository.delete(id)
    return redirect('/cocktails')

