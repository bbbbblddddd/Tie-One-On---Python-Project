DROP TABLE cocktails;
DROP TABLE ingredients;
-- DROP TABLE cocktail_ingredient;

-- CREATE TABLE cocktails (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR (255),
--     description TEXT,
--     instructions TEXT,
--     ingredient_id INT REFERENCES cocktail_ingredient(id) ON DELETE CASCADE,
--     quantity INT
-- );

-- CREATE TABLE ingredients(
--     id SERIAL PRIMARY KEY,
--     ingredient_id INT REFERENCES cocktail_ingredient(id) ON DELETE CASCADE,
--     quantity INT
-- );

-- CREATE TABLE cocktail_ingredient(
--     id SERIAL PRIMARY KEY,    
-- );




CREATE TABLE cocktails (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    description TEXT,
    instructions TEXT,
    ingredient_id INT REFERENCES ingredients.ingredient(id) ON DELETE CASCADE,
    quantit_id INT REFERENCES ingredients.quantity(id)
);

CREATE TABLE ingredients(
    id SERIAL PRIMARY KEY,
    ingredient VARCHAR (255)
    quantity INT
);