from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.cocktail import Cocktail
import repositories.cocktail_repository as cocktail_repository

cocktails_blueprint = Blueprint('cocktails', __name__)

@cocktails_blueprint.route('/cocktails')
def cocktails():
    cocktails = cocktail_repository.select_all()
    return render_template('cocktails/index.html', cocktails = cocktails)

