from hands import YatzyHand

class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)

    def score_twos(self, hand):
        return sum(hand.twos)

    def score_threes(self, hand):
        return sum(hand.threes)

    def score_fours(self, hand):
        return sum(hand.fours)

    def score_fives(self, hand):
        return sum(hand.fives)

    def score_sixes(self, hand):
        return sum(hand.sixes)

    def _score_set(self, hand, set_size):
        scores = []

    def score_yatzy(self, hand):
        if sum(hand.ones) == 5:
            return 50
        if sum(hand.twos) == 10:
            return 50
        if sum(hand.threes) == 15:
            return 50
        if sum(hand.fours) == 20:
            return 50
        if sum(hand.fives) == 25:
            return 50
        if sum(hand.sixes) == 30:
            return 50
        else:
            return 0

    @property
    def full_house(self):
        if all(k in self._sets for k in (2,3)):
            return True
