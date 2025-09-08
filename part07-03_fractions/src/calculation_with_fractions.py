# Write your solution here
from fractions import Fraction
from math import floor 

def fractionate(amount: int) -> list:
    f_list = []
    for i in range(amount):
        f_list.append(Fraction(1, amount))
    return f_list