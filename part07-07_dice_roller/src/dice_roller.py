# Write your solution here
from random import choice

def roll(die: str):
    die_options = {
        'A': [3, 3, 3, 3, 3, 6],
        'B': [2, 2, 2, 5, 5, 5],
        'C': [1, 4, 4, 4, 4, 4]
    }

    return choice(die_options.get(die, []))

def play(die1: str, die2: str, times: int) -> tuple[int]:
    die1_wins = 0
    die2_wins = 0
    ties = 0
    for _ in range(times):
        die1_result = roll(die1)
        die2_result = roll(die2)

        if die1_result > die2_result:
            die1_wins += 1
        elif die1_result < die2_result:
            die2_wins += 1
        else:
            ties += 1
    return (die1_wins, die2_wins, ties)

if __name__ == '__main__':
    result = play('A', 'C', 1000)
    print(result)
    result = play('B', 'B', 1000)
    print(result)
    