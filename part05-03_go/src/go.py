# Write your solution here
def who_won(game_board: list[list]) -> int:
    p1 = sum(row.count(1) for row in game_board)
    p2 = sum(row.count(2) for row in game_board)
    return 0 if p1 == p2 else 1 if p1 > p2 else 2

if __name__  ==  '__main__':
    print(who_won([[1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0]]))