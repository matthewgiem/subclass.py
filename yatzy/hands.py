from dice import D6


class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super(Hand, self).__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()

class YatzyHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=6, die_class=D6, *args, **kwargs)
