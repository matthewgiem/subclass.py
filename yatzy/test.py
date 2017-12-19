from hands import YatzyHand
from hands import Hand
import dice

die = dice.Die(sides=5)
print(die.value)
D6 = dice.D6()
print(D6.value)
hand = Hand(size=5, die_class=dice.D6)
print(type(hand))
print(hand)
