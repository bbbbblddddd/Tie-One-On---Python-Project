from db.run_sql import run_sql

from models.cocktail import Cocktail
from models.ingredient import Ingredient

def save(ingredient):
    sql = "INSERT INTO ingredients (name) VALUES (%s) RETURNING id"
    values = [ingredient.name]
    results = run_sql( sql, values )
    ingredient.id = results[0]['id']
    return ingredient

def select_all():
    ingredients = []

    sql = "SELECT * FROM ingredients"
    results = run_sql(sql)

    for row in results:
        ingredient = Ingredient(row['name'], row['id'])
        ingredients.append(ingredient)
    return ingredients

def select(id):
    ingredient = None
    sql = "SELECT * FROM ingredients WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        ingredient = Ingredient(result['name'], result['id'] )
    return ingredient

def cocktails(ingredient):
    cocktail_ingredients = []
    sql = "SELECT cocktails.* FROM cocktails INNER JOIN cocktail_ingredient ON cocktail_ingredient.cocktail_id = cocktails.id WHERE ingredient_id = %s "
    values = [ingredient.id]
    results = run_sql(sql,values)

    for row in results:
        cocktail = Cocktail (row['name'], row['description'], row['instructions'], row ['id'])
        cocktail_ingredients.append(cocktail)
    return cocktail_ingredients

def delete_all():
    sql = "DELETE FROM ingredients"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM ingredients WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select_by_cocktail(cocktail_id):
    query = 'SELECT * FROM ingredients WHERE cocktail_id = ?'
    params = (cocktail_id,)
    results = run_sql(query, params)

    return [Ingredient(*row) for row in results]




