from db.run_sql import run_sql

from models.cocktail import Cocktail


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
    sql = "SELECT * FROM cockatils WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        cocktail = Cocktail(result['name'], result ['description'], result['instructions'], result['id'])
        return cocktail

# def users(location):
#     users = []

#     sql = "SELECT users.* FROM users INNER JOIN visits ON visits.user_id = users.id WHERE location_id = %s"
#     values = [location.id]
#     results = run_sql(sql, values)

#     for row in results:
#         user = User(row['name'], row['id'])
#         users.append(user)

#     return users

def delete_all():
    sql = "DELETE FROM cocktails"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cocktails WHERE id = %s"
    values = [id]
    run_sql(sql, values)