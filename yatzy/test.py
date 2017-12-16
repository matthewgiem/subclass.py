from hands import YatzyHand
from dice import D6
from dice import Die
from hands import Hand

die = Die(sides=5)
print(die.value)
D6 = D6()
print(D6.value)
hand = Hand(size=5, die_class=D6)
