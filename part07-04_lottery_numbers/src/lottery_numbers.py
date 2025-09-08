# Write your solution here
from random import sample

def lottery_numbers(amount: int, lower: int, upper: int) -> list[int]:
    choice_list = list(range(lower, upper + 1))
    chosen = sorted(sample(choice_list, amount))
    return chosen