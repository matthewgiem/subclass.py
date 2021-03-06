import random

class Die(object):

    def __init__(self, sides=2, value=0):
        if not sides >=2:
            raise ValueError("We must have at least 2 sides")
        if not isinstance(sides, int):
            raise ValueError("The sides must be an integer")
        if not isinstance(value, int):
            raise ValueError("the value must be an integer")
        self.value = value or random.randint(1, sides)

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return not int(self) == other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) >= other

    def __le__(self, other):
        return int(self) <= other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)


class D6(Die):
    def __init__(self, sides=6, value=0):
         super(D6, self).__init__(sides=6)
