class Cocktail:
    def __init__(self, name, description, instructions, image_url=None, id=None):

        self.name = name
        self.description = description
        self.instructions = instructions
        self.image_url = image_url
        self.id = id
        self.ingredients = []
