import pdb

from models.ingredient import Ingredient
from models.cocktail import Cocktail

import repositories.cocktail_repository as cocktail_repository
import repositories.ingredient_repository as ingredient_repository
import repositories.cocktail_ingredient_repository as cocktail_ingredient_repository

cocktail_repository.delete_all()
ingredient_repository.delete_all()
cocktail_ingredient_repository.delete_all()

gimlet = Cocktail('Gimlet', 'A lime-heavy, classic gin cocktail with a rich naval history and a sharp kick.',
                  'Add the 60 ml of gin, 30ml of lime juice and 30ml of sugar syrup to a shaker with ice and shake until well-chilled. Strain into a chilled cocktail glass or an rocks glass filled with fresh ice. Garnish with a lime wheel.', 'https://i.imgur.com/lIekaw4.jpg')
cocktail_repository.save(gimlet)

margerita = Cocktail('Margerita', 'Combining the tang of lime and the sweetness of orange liqueur with the distinctive strength of tequila.', 'Add 60ml of Tequila, 15ml of Triple Sec, 30ml of Lime Juice and 15ml of Sugar Syrup to a cocktail shaker filled with ice, and shake until well-chilled. Strain into a rocks glass over fresh ice. Garnish with a lime wheel and kosher salt rim or Tajin rim.')
cocktail_repository.save(margerita)

manhattan = Cocktail('Manhattan', 'The Manhattan is a classic cocktail of choice for whiskey-lovers.', 'Add the 60ml of Bourbon, 30ml Vermouth, and 2-3 dashes of Angustura Bitters into a mixing glass with ice and stir until well-chilled. Strain into a chilled Nick & Nora or Coupe glass. Garnish with a brandied cherry')
cocktail_repository.save(manhattan)

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



cocktail_ingredient_repository.save(sugar_syrup.id, gimlet.id)
cocktail_ingredient_repository.save(gin.id, gimlet.id)
cocktail_ingredient_repository.save(lime_juice.id,gimlet.id)


cocktail_ingredient_repository.save(tequila.id, margerita.id)
cocktail_ingredient_repository.save(lime_juice.id, margerita.id)
cocktail_ingredient_repository.save(triple_sec.id, margerita.id)
cocktail_ingredient_repository.save(sugar_syrup.id, margerita.id)

cocktail_ingredient_repository.save(bourbon.id, manhattan.id)
cocktail_ingredient_repository.save(vermouth.id, manhattan.id)
cocktail_ingredient_repository.save(angustura_bitters.id, manhattan.id)

pdb.set_trace()
