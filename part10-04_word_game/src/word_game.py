# Write your solution here
import random


class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return -1


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiou"
        p1_v_count = 0
        p2_v_count = 0

        for char in player1_word:
            if char in vowels:
                p1_v_count += 1

        for char in player2_word:
            if char in vowels:
                p2_v_count += 1

        if p1_v_count > p2_v_count:
            return 1
        elif p1_v_count < p2_v_count:
            return 2
        else:
            return -1


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        winning_hands = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        p1_beats = winning_hands.get(player1_word)
        p2_beats = winning_hands.get(player2_word)
        if p1_beats is None and p2_beats is None or player1_word == player2_word:
            return -1
        elif p1_beats is not None and p2_beats is None or p1_beats == player2_word:
            return 1
        elif p2_beats is not None and p1_beats is None or p2_beats == player1_word:
            return 2
        # Make type check happy
        else:
            return -1


if __name__ == "__main__":
    p = RockPaperScissors(4)
    p.play()
