from db.run_sql import run_sql

from models.cocktail import Cocktail
from models.ingredient import Ingredient



def save(cocktail):
    sql = "INSERT INTO cocktails(name, description, instructions) VALUES ( %s, %s, %s ) RETURNING id"
    values = [cocktail.name, cocktail.description, cocktail.instructions]
    results = run_sql( sql, values )
    cocktail.id = results[0]['id']
    return cocktail

def select_all():
    cocktails = []

    sql = "SELECT * FROM cocktails"
    results = run_sql(sql)
    for row in results:
        cocktail = Cocktail(row['name'], row['description'], row['instructions'], row['id'])
        cocktails.append(cocktail)
    return cocktails

def select(id):
    cocktail = None
    sql = "SELECT * FROM cocktails WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        cocktail = Cocktail(result['name'], result ['description'], result['instructions'], result['id'])
        return cocktail

def ingredients(cocktail):
    cocktail_ingredients = []
    sql = "SELECT ingredients.* FROM ingredients INNER JOIN cocktail_ingredient ON cocktail_ingredient.ingredient_id = ingredients.id WHERE cocktail_id = %s "
    values = [cocktail.id]
    results = run_sql(sql,values)

    for row in results:
        ingredient = Ingredient (row['name'], row ['id'])
        cocktail_ingredients.append(ingredient)
    return cocktail_ingredients

def delete_all():
    sql = "DELETE FROM cocktails"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cocktails WHERE id = %s"
    values = [id]
    run_sql(sql, values)