import unittest

from models.cocktail import Cocktail

class TestCocktail(unittest.TestCase):

    def setUp(self):
        self.cocktail = Cocktail('gimlet', 'gin heavy favourite', 'shake and pour')

    def test_cocktail_has_name(self):
        self.assertEqual('gimlet', self.cocktail.name)
