class Cocktail:
    def __init__(self, name, description, instructions, id = None):

        self.name = name
        self.description = description
        self.instructions = instructions
        self.id = id
        self.ingredients = []
        self.quantitiy = []
