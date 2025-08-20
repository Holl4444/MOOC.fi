# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    if not (0 <= x < len(game_board)) or not (0 <= y < len(game_board)) or game_board[y][x] != '':
        return False
    game_board[y][x] = piece
    return True

if __name__ == '__main__':
    game_board = [["", "", ""], ["X", "X", "O"], ["O", "O", "X"]]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)