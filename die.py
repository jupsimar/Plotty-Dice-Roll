from random import randint 

class Die:
    """ a class that rolls a single die """

    def __init__(self, num_sides=6):
        """ 6 sided die """
        self.num_sides = num_sides

    def roll(self):
        """ rolling return """
        return randint(1, self.num_sides)

        