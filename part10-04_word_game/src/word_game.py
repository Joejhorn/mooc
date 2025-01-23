# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
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
                pass # it's a tie

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
            pass
        
class MostVowels(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)
        self.VOWELS = ['A', 'E', 'I', 'O', 'U']
    
    def round_winner(self, player1_word, player2_word):
        count1 = 0
        count2 = 0
        player1_word = player1_word.upper()
        player2_word = player2_word.upper()
        for vowel in self.VOWELS:
            count1 += player1_word.count(vowel)
            count2 += player2_word.count(vowel)
        if count1 > count2:
            return 1
        elif count2 > count1:
            return 2
        else:
            pass

class RockPaperScissors(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)
    def round_winner(self, player1_word, player2_word):
        options = ['ROCK', 'PAPER', 'SCISSORS']
        options2 = {'ROCK':'PAPER', 'PAPER': 'SCISSORS', 'SCISSORS': 'ROCK'}
        player2_word = player2_word.upper()
        player1_word = player1_word.upper()
        if player1_word in options and player2_word in options:
            if player1_word == 'ROCK' and player2_word == options2['ROCK']:
                return 2
            elif player1_word == 'PAPER' and player2_word == options2['PAPER']:
                return 2
            elif player1_word == 'SCISSORS' and player2_word == options2['SCISSORS']:
                return 2
            elif player1_word == player2_word:
                pass
            else:
                return 1
        elif player1_word in options:
            return 1
        elif player2_word in options:
            return 2
        
            
    



if __name__ == '__main__':
    p = RockPaperScissors(3)
    p.play()