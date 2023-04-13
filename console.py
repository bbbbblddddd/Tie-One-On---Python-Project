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
                  'Add the 60 ml of gin, 30ml of lime juice and 30ml of sugar syrup to a shaker with ice and shake until well-chilled. Strain into a chilled cocktail glass or an rocks glass filled with fresh ice. Garnish with a lime wheel.', 'https://i.imgur.com/iFmyUdo.png')
cocktail_repository.save(gimlet)

margerita = Cocktail('Margerita', 'Combining the tang of lime and the sweetness of orange liqueur with the distinctive strength of tequila.',
                     'Add 60ml of Tequila, 15ml of Triple Sec, 30ml of Lime Juice and 15ml of Sugar Syrup to a cocktail shaker filled with ice, and shake until well-chilled. Strain into a rocks glass over fresh ice. Garnish with a lime wheel and kosher salt rim or Tajin rim.', 'https://i.imgur.com/hemYzqt.png')
cocktail_repository.save(margerita)

manhattan = Cocktail('Manhattan', 'The Manhattan is a classic cocktail of choice for whiskey-lovers.',
                     'Add the 60ml of Bourbon, 30ml Vermouth, and 2-3 dashes of Angustura Bitters into a mixing glass with ice and stir until well-chilled. Strain into a chilled Nick & Nora or Coupe glass. Garnish with a brandied cherry', 'https://i.imgur.com/3kB2NLr.png')
cocktail_repository.save(manhattan)

# whisky_sour = Cocktail(
#     'Whisky Sour', 'A smooth cocktail with a hint of citrus sourness and an invigorating blast of whisky',  )

eastside_gimlet = Cocktail('East Side Gimlet', 'A riff on the "Southside" cocktail that incorporates cucmumber aswell as mint',
                           'Muddle 2 thick cucumber slices and 6 - 8 mint leaves in base of shaker. Add 60ml gin, 22.5ml lime juice, 22.5ml sugar syrup, Shake with ice and fine strain into chilled glass. Garnish with a mint leaf')
cocktail_repository.save(eastside_gimlet)


gin = Ingredient ('Gin')
ingredient_repository.save(gin)

tequila = Ingredient('Tequila')
ingredient_repository.save(tequila)

bourbon = Ingredient('Bourbon')
ingredient_repository.save(bourbon)

whisky = Ingredient('Whisky')
ingredient_repository.save(whisky)

rum = Ingredient('Rum')
ingredient_repository.save(rum)

vermouth = Ingredient('Vermouth')
ingredient_repository.save(vermouth)

lime_juice = Ingredient('Lime Juice')
ingredient_repository.save(lime_juice)

triple_sec = Ingredient('Triple Sec')
ingredient_repository.save(triple_sec)

lemon_juice = Ingredient('Lemon Juice')
ingredient_repository.save(lemon_juice)

sugar_syrup = Ingredient('Sugar Syrup')
ingredient_repository.save(sugar_syrup)

angustura_bitters = Ingredient ('Angustura Bitters')
ingredient_repository.save(angustura_bitters)

cucumber = Ingredient('Cucumber Slices')
ingredient_repository.save(cucumber)

mint = Ingredient('Mint Leaves')
ingredient_repository.save(mint)

egg = Ingredient('Egg White')
ingredient_repository.save(egg)




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

cocktail_ingredient_repository.save(gin.id, eastside_gimlet.id)
cocktail_ingredient_repository.save(lime_juice.id, eastside_gimlet.id)
cocktail_ingredient_repository.save(sugar_syrup.id, eastside_gimlet.id)
cocktail_ingredient_repository.save(cucumber.id, eastside_gimlet.id)
cocktail_ingredient_repository.save(mint.id, eastside_gimlet.id)

pdb.set_trace()
