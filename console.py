import pdb

from models.ingredient import Ingredient
from models.cocktail import Cocktail

import repositories.cocktail_repository as cocktail_repository
import repositories.ingredient_repository as ingredient_repository
import repositories.cocktail_ingredient_repository as cocktail_ingredient_repository

cocktail_repository.delete_all()
ingredient_repository.delete_all()
cocktail_ingredient_repository.delete_all()

# gimlet = Cocktail('Gimlet', 'A lime-heavy, classic gin cocktail with a rich naval history and a sharp kick.',
#                   'Add the 60 ml of gin, 30ml of lime juice and 30ml of sugar syrup to a shaker with ice and shake until well-chilled. Strain into a chilled cocktail glass or an rocks glass filled with fresh ice. Garnish with a lime wheel.', 'https://i.imgur.com/iFmyUdo.png')
# cocktail_repository.save(gimlet)

margerita = Cocktail('Tommys Margarita', 'Replaces Triple Sec with Agave Syrup and Orange peel to create a natural fresh variant of the traditional Margarita',
                     'Add 60ml of Tequila, 30ml of Lime Juice, 15ml Agave Syrup and 1-2 peels of fresh orange to a cocktail shaker filled with ice and shake until well-chilled then strain into a Margarita glass. Garnish with a lime wheel and kosher salt rim or Tajin rim.', 'https://i.imgur.com/VMEjljo.png')
cocktail_repository.save(margerita)

# manhattan = Cocktail('Manhattan', 'The Manhattan is a classic cocktail of choice for whiskey lovers.',
#                      'Add the 60ml of Bourbon, 30ml Vermouth, and 2-3 dashes of Angustura Bitters into a mixing glass with ice and stir until well-chilled. Strain into a chilled Nick & Nora or Coupe glass. Garnish with a brandied cherry', 'https://i.imgur.com/3kB2NLr.png')
# cocktail_repository.save(manhattan)

eastside_gimlet = Cocktail('East Side Gimlet', 'A riff on the Southside cocktail that incorporates cucmumber aswell as mint',
                           'Muddle 2 thick cucumber slices and 6 to 8 mint leaves in base of shaker. Add 60ml gin, 22.5ml lime juice, 22.5ml sugar syrup, Shake with ice and fine strain into chilled coupe glass. Garnish with a mint leaf', 'https://i.imgur.com/dG2Ta1l.png')
cocktail_repository.save(eastside_gimlet)

robroy = Cocktail('Rob Roy', 'A Scottish Manhattan that uses blended whisky instead of Bourbon. Best enjoyed at Hogmanay!',
                  'Combine 60ml of blended whisky, 22ml of sweet vermouth adn two dashes of Angustura Bitters in a mixing glass with ice. Stir for 30 seconds until well chilled, strain into a coupe glass and garnish with a cherry or lemon twist.', 'https://i.imgur.com/eHgNxxr.png')
cocktail_repository.save(robroy)

commoncold = Cocktail('Common Cold', 'Honey and lemon used to create the perfect cold remedy that hints at the flavour of Calpol cough medicine', 'Combine 60ml Puerto De Indias Strawberry Gin, 22.5ml Lemon Juice, 15ml Honey Syrup, 7.5ml Grenadine and one egg white to a shaker. Vigorously dry shake for 15 seconds. Add ice then shake until chilled. Serve and strain in a coupe glass.', 'https://i.imgur.com/pKbx4tO.png'  )
cocktail_repository.save(commoncold)

paperplane = Cocktail ('Paper Plane', 'A riff on the equal-parts brilliance of "The Last Word" cocktail and named after the M.I.A track of the same name', 'Combine 22ml of Bourbon, Lemon Juice, Aperol and Amaro Nonino in a shaker. Shake with ice and fine strain into chilled coupe glass.', 'https://i.imgur.com/3f35gRG.png' )
cocktail_repository.save(paperplane)

whisky_sour = Cocktail(
    'Whisky Sour', 'A smooth cocktail with a hint of citrus sourness and an invigorating blast of rye whisky', 'Combine 60ml Bourbon, 22ml Lemon Juice, 22ml Sugar Syrup and one egg white in a shaker. Dry shake to emulsify egg white, then add ice and shake until well chilled. STain and serve in a rocks glass with one large ice cube.', 'https://i.imgur.com/tcBjWxR.png' )
cocktail_repository.save(whisky_sour)

twelvemile = Cocktail('12 Mile Limit', 'A grenadine heavy, prohibition era sipper using equal parts of each ingredient', 'Combine 30ml of Bourbon, Cognac, Grenadine and Lemon Juice with ice to a cocktail shaker. Shake until chilled and strain ito a coupe glass', 'https://i.imgur.com/0sBTbRd.png')
cocktail_repository.save(twelvemile)

silverlining = Cocktail ('Silver Lining', 'A rye fizz created at Milk and Honey in New York using spanish liqeur Licor 43', 'Combine 45ml Bourbon, 22ml Lemon Juice, 22ml Licor 43 and one egg white in a shaker. Dry shake to emulsify egg white, then add ice and shake until well chilled. Strain into a highball glass with ice then top with soda water. Let stand for a moment so the foam settles, then add more soda to raise the froth above the rim of the glass', 'https://i.imgur.com/yWsh521.png')
cocktail_repository.save(silverlining)



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

cognac = Ingredient('Cognac')
ingredient_repository.save(cognac)

lime_juice = Ingredient('Lime Juice')
ingredient_repository.save(lime_juice)

lemon_juice = Ingredient('Lemon Juice')
ingredient_repository.save(lemon_juice)

triple_sec = Ingredient('Triple Sec')
ingredient_repository.save(triple_sec)

licor43 = Ingredient('Licor 43')
ingredient_repository.save(licor43)

amaro = Ingredient('Amaro Nonino')
ingredient_repository.save(amaro)

aperol = Ingredient('Aperol')
ingredient_repository.save(aperol)

angustura_bitters = Ingredient ('Angustura Bitters')
ingredient_repository.save(angustura_bitters)

sugar_syrup = Ingredient('Sugar Syrup')
ingredient_repository.save(sugar_syrup)

honey = Ingredient('Honey Syrup')
ingredient_repository.save(honey)

agave = Ingredient('Agave Syrup')
ingredient_repository.save(agave)

gren = Ingredient('Grenadine')
ingredient_repository.save(gren)

cucumber = Ingredient('Cucumber Slices')
ingredient_repository.save(cucumber)

orangepeel = Ingredient('Orange Peel')
ingredient_repository.save(orangepeel)

mint = Ingredient('Mint Leaves')
ingredient_repository.save(mint)

egg = Ingredient('Egg White')
ingredient_repository.save(egg)

soda = Ingredient('Soda Water')
ingredient_repository.save(soda)










# cocktail_ingredient_repository.save(sugar_syrup.id, gimlet.id)
# cocktail_ingredient_repository.save(gin.id, gimlet.id)
# cocktail_ingredient_repository.save(lime_juice.id,gimlet.id)

cocktail_ingredient_repository.save(tequila.id, margerita.id)
cocktail_ingredient_repository.save(lime_juice.id, margerita.id)
cocktail_ingredient_repository.save(agave.id, margerita.id)
cocktail_ingredient_repository.save(orangepeel.id, margerita.id)

cocktail_ingredient_repository.save(bourbon.id, whisky_sour.id)
cocktail_ingredient_repository.save(lemon_juice.id, whisky_sour.id)
cocktail_ingredient_repository.save(sugar_syrup.id, whisky_sour.id)
cocktail_ingredient_repository.save(egg.id, whisky_sour.id)

# cocktail_ingredient_repository.save(bourbon.id, manhattan.id)
# cocktail_ingredient_repository.save(vermouth.id, manhattan.id)
# cocktail_ingredient_repository.save(angustura_bitters.id, manhattan.id)

cocktail_ingredient_repository.save(gin.id, eastside_gimlet.id)
cocktail_ingredient_repository.save(lime_juice.id, eastside_gimlet.id)
cocktail_ingredient_repository.save(sugar_syrup.id, eastside_gimlet.id)
cocktail_ingredient_repository.save(cucumber.id, eastside_gimlet.id)
cocktail_ingredient_repository.save(mint.id, eastside_gimlet.id)

cocktail_ingredient_repository.save(whisky.id, robroy.id)
cocktail_ingredient_repository.save(vermouth.id, robroy.id)
cocktail_ingredient_repository.save(angustura_bitters.id, robroy.id)

cocktail_ingredient_repository.save(bourbon.id, paperplane.id)
cocktail_ingredient_repository.save(lemon_juice.id, paperplane.id)
cocktail_ingredient_repository.save(aperol.id, paperplane.id)
cocktail_ingredient_repository.save(amaro.id, paperplane.id)

cocktail_ingredient_repository.save(gin.id, commoncold.id)
cocktail_ingredient_repository.save(lemon_juice.id, commoncold.id)
cocktail_ingredient_repository.save(honey.id, commoncold.id)
cocktail_ingredient_repository.save(gren.id, commoncold.id)
cocktail_ingredient_repository.save(egg.id, commoncold.id)

cocktail_ingredient_repository.save(bourbon.id, twelvemile.id)
cocktail_ingredient_repository.save(cognac.id, twelvemile.id)
cocktail_ingredient_repository.save(gren.id, twelvemile.id)
cocktail_ingredient_repository.save(lemon_juice.id, twelvemile.id)

cocktail_ingredient_repository.save(bourbon.id, silverlining.id)
cocktail_ingredient_repository.save(lemon_juice.id, silverlining.id)
cocktail_ingredient_repository.save(licor43.id, silverlining.id)
cocktail_ingredient_repository.save(soda.id, silverlining.id)




pdb.set_trace()
