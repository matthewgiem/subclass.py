from dice import D6


class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super(Hand, self).__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()

        def _by_value(self, value):
            dice = []
            for die in self:
                if die == value:
                    dice.append(die)
            return dice


class YatzyHand(Hand):
    def __init__(self, *args, **kwargs):
        super(YatzyHand, self).__init__(size=6, die_class=D6, *args, **kwargs)

    @property
    def ones(self):
        return self._by_value(1)

    @property
    def twos(self):
        return self._by_value(2)

    @property
    def threes(self):
        return self._by_value(3)

    @property
    def fours(self):
        return self._by_value(4)

    @property
    def fives(self):
        return self._by_value(5)

    @property
    def sixs(self):
        return self._by_value(6)
