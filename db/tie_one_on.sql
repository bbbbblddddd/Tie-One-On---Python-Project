DROP TABLE cocktail_ingredient;
DROP TABLE cocktails;
DROP TABLE ingredients;

CREATE TABLE cocktails (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    description TEXT,
    instructions TEXT
);

CREATE TABLE ingredients(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cocktail_ingredient(
    id SERIAL PRIMARY KEY,
    ingredient_id INT REFERENCES ingredients(id) ON DELETE CASCADE,
    cocktail_id INT REFERENCES cocktails(id) ON DELETE CASCADE
);


