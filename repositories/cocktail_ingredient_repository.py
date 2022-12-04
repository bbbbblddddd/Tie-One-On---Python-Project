from db.run_sql import run_sql

from models.cocktail import Cocktail
from models.ingredient import Ingredient

import repositories.ingredient_repository as ingredient_repository
import repositories.cocktail_repository as cocktail_repository


def save(cocktail_ingredient):
    sql = "INSERT INTO cocktail_ingredient ( ingredient_id, cocktail_id ) VALUES ( %s, %s) RETURNING id"
    values = [cocktail_ingredient.ingredient.id, cocktail_ingredient.cocktail.id]
    results = run_sql( sql, values )
    cocktail_ingredient.id = results[0]['id']
    return cocktail_ingredient

def select_all():
    cocktail_ingredients = []

    sql = "SELECT * FROM cocktail_ingredient"
    results = run_sql(sql)

    for row in results:
        ingredient = ingredient_repository.select(row['ingredient_id'])
        cocktail = cocktail_repository.select(row['cocktail_id'])
        cocktail_ingredient = (ingredient, cocktail, row['id'])
        cocktail_ingredients.append(cocktail_ingredient)
    return cocktail_ingredients
# could have errors regarding syntax

def cocktail(cocktail_ingredient):
    sql = "SELECT * FROM cocktails WHERE id = %s"
    values = [cocktail_ingredient.cocktail.id]
    results = run_sql(sql, values)[0]
    cocktail = Cocktail(results['name'], results['description'], results['instructions'], results['id'])
    return cocktail

def ingredient(cocktail_ingredient):
    sql = "SELECT * FROM ingredients WHERE id = %s"
    values = [cocktail_ingredient.ingredient.id]
    results = run_sql(sql, values)[0]
    ingredient = Ingredient(results['name'], results['id'])
    return ingredient

def delete_all():
    sql = "DELETE FROM cocktail_ingredient"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cocktail_ingredient WHERE id = %s"
    values = [id]
    run_sql(sql, values)