from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.ingredient import Ingredient

ingredients_blueprint = Blueprint('ingredients', __name__)
