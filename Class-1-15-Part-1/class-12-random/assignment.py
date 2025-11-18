'''
Dice Roll Simulation
Simulate rolling a six-sided die 10 times and print each result.
'''
from random import choice
die=[1,2,3,4,5,6]

for index in range(1,11):
    print("Roll-",index,"Die Result-",choice(die))
