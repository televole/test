
import random

# The Player class is the parent class for all type of players: human, random, reflect, rock cycle"""

class Player:

    moves = ['rock', 'paper', 'scissors']

    def move(self, my_move):

        return my_move

    def learn(self, my_move, opp_move):

        print(f"Player 1 played {my_move} in the previous round.\n")
        print(f"Player 2 played {opp_move} in the previous round.\n")

        return my_move, opp_move


class Human(Player):
    def move(self, my_move, opp_move):

        human_move = input("Please make your choice! ").lower()

        while human_move not in self.moves:

            human_move = input("Please make your choice! ").lower()

        return human_move


class Rock(Player):

    def move(self, my_move, opp_move):
        return 'rock'


class Reflect(Player):

    def move(self, my_move, opp_move):

        if opp_move == self.moves[0]:

            return self.moves[0]

        elif opp_move == self.moves[1]:

            return self.moves[1]

        elif opp_move == self.moves[2]:

            return self.moves[2]

        elif opp_move == self.moves[3]:

            return self.moves[3]

        else:

            return self.moves[4]


class Random(Player):

    def move(self, my_move, opp_move):

        return random.choice(self.moves)


class Cycle(Player):

    def move(self, my_move, opp_move):

        return {
            'rock': 'paper',
            'paper': 'scissors',
            'scissors': 'rock'
            }[my_move]

class Game:

    def __init__(self, p1, p2):

        self.p1 = p1

        self.p2 = p2

    def scores(self, winner, p1_last, p2_last):

        '''Display a scores and updated player scores.'''
        if winner == 1:

            p1_current = p1_last + 1

            print("Scores")

            print(f"Player 1: {p1_current} | Player 2: {p2_last}")

            return p1_current, p2_last

        elif winner == 2:

            p2_current = p2_last + 1

            print("scores")

            print(f"Player 1: {p1_last} | Player 2: {p2_current}")          

            return p1_last, p2_current

        else:

            print("scores")           

            print(f"Player 1: {p1_last} | Player 2: {p2_last}")

            return p1_last, p2_last

    def winner(self, p1_move, p2_move):

        '''Compute the winner of a round.'''

        if p1_move == p2_move:
            return print("A TIE!\n"), 0
        elif p1_move == 'rock' and p2_move == 'scissors':
            return print("Player 1 Won!!\n"), 1
            
        elif p1_move == 'paper' and p2_move == 'rock':
            return print("Player 1 Won!!\n"), 1
        elif p1_move == 'scissors' and p2_move == 'paper':
            return print("Player 1 Won!!\n"), 1
        else:
            return print("Player 2 Won!!\n"), 2

    def final(self, p1_score, p2_score):

        """
        Display scores.
        """
        print("Scores_\n")
        print(f"Player 1: {p1_score} | Player 2: {p2_score}")
     

        if p1_score == p2_score:

            print('A Tie!')

        elif p1_score > p2_score:

            print('Player 1 won!')

        else:

            print("Player 2 won!")

    def play_round(self, current_rnd, final_rnd, p1_last, p2_last):

        '''Print and return the moves of two player.'''

        if current_rnd == 1:

            p1_move = self.p1.move('scissors', 'paper')

            p2_move = self.p2.move('scissors', 'rock')

            print(f"Player 1: {p1_move} \nPlayer 2: {p2_move}\n")

            return p1_move, p2_move

        else:

            p1_move = self.p1.move(p1_last, p2_last)

            p2_move = self.p2.move(p2_last, p1_last)

            print(f"Player 1: {p1_move} \nPlayer 2: {p2_move}\n")

            return p1_move, p2_move

    def input_number(self, message):
        while True:
            try:
                self.userInput = int(input(message))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return self.userInput
                break

    def play_match(self):

        """
        Play a match with multiple games as user's choice.
        """

        rounds = self.input_number("How many times will you play? ")

        p1_score, p2_score = 0, 0

        p1_last = 'rock'

        p2_last = 'scissors'

        for current_round in range(1, rounds+1):

            print(f"\n___________\n\n Round {current_round }\n___________\n")

            p1_move, p2_move = self.play_round(current_round, rounds, p1_last, p2_last)

            winning_player = self.winner(p1_move, p2_move)

            p1_score, p2_score = self.scores(winning_player, p1_score, p2_score)

            p1_last, p2_last = self.p1.learn(p1_move, p2_move)

            
        self.final(p1_score, p2_score)

        print("\nGame Over")


match_list = ["rock", "random", "reflect", "cycle"]

title = "Rock Paper Scissors\n"

rules = """Rock beats scissors, scissors beats paper, paper beats rock\n"""

types = """Please choose your player type!:\n
Human: User moves with his/her choice

Random: Random moves out of 3 selections

Reflect: opponent's last move

Rock: always selects/plays rock

Cycle: plays rock, paper, and scissors in order"""

matchers = {'human': Human(), 'rock': Rock(), 'random': Random(), 'reflect':Reflect(),'cycle': Cycle()}

print(title)
print(rules, "\n")
print(types, "\n")

match = input("Would you like to play a random match (Y) or a match with your choice(N)? Y/N ")

if match == "Y" or match == "y":

    player1 = random.choice(match_list)
    player2 = random.choice(match_list)

    print(f"Player 1: {player1} Player 2: {player2}\n")

else:
    player1 = input("Who is Player 1? ").lower()
    player2 = input("Who is Player 2? ").lower()

    while player1 not in matchers or player2 not in matchers:

        player1 = input("Who is Player 1? ").lower()
        player2 = input("Who is Player 2? ").lower()

game = Game(matchers[player1], matchers[player2])
game.play_match()

