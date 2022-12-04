import pdb

from models.ingredient import Ingredient
from models.cocktail import Cocktail

import repositories.cocktail_repository as cocktail_repository
import repositories.ingredient_repository as ingredient_repository
import repositories.cocktail_ingredient_repository as cocktail_ingredient_repository

cocktail_repository.delete_all()
ingredient_repository.delete_all()
cocktail_ingredient_repository.delete_all()

cocktail1 = Cocktail('Gimlet', 'A lime-heavy, classic gin cocktail with a rich naval history and a sharp kick.', 'place all ingredients in a cocktail shaker with ice. shake, pour')
cocktail_repository.save(cocktail1)

cocktail2 = Cocktail('Margerita', 'Combining the tang of lime and the sweetness of orange liqueur with the distinctive strength of tequila, the classic Margarita strikes all of the right keys.', 'place all ingredients in a cocktail shaker with ice. shake, pour')
cocktail_repository.save(cocktail2)

cocktail3 = Cocktail('Manhattan', 'The Manhattan is a classic cocktail of choice for whiskey-lovers.', 'place all ingredients in a cocktail shaker with ice. shake, pour')
cocktail_repository.save(cocktail3)

# could I rename these variable say... cocktail_gimlet, cocktail_margerita etc to make it more readable? Is this advised?
# also what was the input in ordet to take a line during a string? My description TEXT field's are v.lomg and it makees it hard to navigate through + edit

gin = Ingredient ('Gin')
ingredient_repository.save(gin)

lime_juice = Ingredient ('Lime Juice')
ingredient_repository.save(lime_juice)

sugar_syrup = Ingredient ('Sugar Syrup')
ingredient_repository.save(sugar_syrup)

tequila = Ingredient ('Tequila')
ingredient_repository.save(tequila)

triple_sec = Ingredient ('Triple Sec')
ingredient_repository.save(triple_sec)

bourbon = Ingredient ('Bourbon')
ingredient_repository.save(bourbon)

vermouth = Ingredient ('Vermouth')
ingredient_repository.save(vermouth)

angustura_bitters = Ingredient ('Angustura Bitters')
ingredient_repository.save(angustura_bitters)



gimlet = (cocktail1, gin, lime_juice, sugar_syrup)
cocktail_ingredient_repository.save(gimlet)

margerita = (cocktail2, tequila, lime_juice, triple_sec, sugar_syrup)
cocktail_ingredient_repository.save(margerita)

manhattan = (cocktail3, bourbon, vermouth, angustura_bitters)
cocktail_ingredient_repository.save(manhattan)
 
# is syntax above correct for joining tables together?

pdb.set_trace()

# what is the purpose of set trace? and is it convention?