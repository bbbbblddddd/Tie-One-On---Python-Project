from db.run_sql import run_sql

from models.cocktail import Cocktail
from models.ingredient import Ingredient

import repositories.ingredient_repository as ingredient_repository
import repositories.cocktail_repository as cocktail_repository
import repositories.cocktail_ingredient_repository as cocktail_ingredient_repository


# def save(cocktail_ingredient, cocktail):
#     sql = "INSERT INTO cocktail_ingredient ( ingredient_id, cocktail_id ) VALUES ( %s, %s) RETURNING id"
#     values = [cocktail_ingredient.id, cocktail.id]
#     run_sql( sql, values )

    
def save(cocktail_ingredient, cocktail):
    sql = "INSERT INTO cocktail_ingredient ( ingredient_id, cocktail_id ) VALUES ( %s, %s) RETURNING id"
    values = [cocktail_ingredient, cocktail]
    run_sql( sql, values )
    
def select_all_by_cocktail_id(id):
    sql = "SELECT * FROM cocktail_ingredient WHERE cocktail_id = %s"
    values = [id]
    results = run_sql(sql, values)
    ingredients = []
    for row in results:
        # select ingredient from ingredient repository
        ingredient = ingredient_repository.select(row['ingredient_id'])
        ingredients.append(ingredient)
    return ingredients 


 


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