"""
Write a program to simulate a game of Rock, Paper, Scissors.
The game will prompt the player to choose rock, paper, or scissors by typing 'r',
'p', or 's'. The computer will randomly select its choice. The game will then display
both choices using emojis and determine the winner based on the rules.


Optional Enhancements
• Modify the game so that the first player (or computer) to win two out of three
rounds is declared the overall winner. This adds a competitive aspect to the
game.
• Keep a tally of how many times the player wins, loses, or ties with the
computer. Display these statistics at the end of the game.
• Add an option for two players to play against each other, taking turns to input
their choices. The program should then determine the winner based on their
inputs.
"""

import random
from enum import Enum, auto, Flag


class RockPaperScissors(Enum):
    rock = "r"
    paper = "p"
    scissors = "s"

class Results(Flag):
    lose = auto()
    equal = auto()
    win = auto()
    
class Player:
    
    def __init__(self, name: str, isComputer: bool):
        self.name = name
        self.isComputer = isComputer
        self.choice = RockPaperScissors.paper

    def __inputChoice(self):
        while True:
            try:
                self.choice = RockPaperScissors(input("input your choice {r, p, s}: "))
                break
            except ValueError:
                print("Invalid data, please input again!! ")
    
    def getChoice(self) -> RockPaperScissors:
        return self.choice
    
    def play(self):
        if self.isComputer:
            self.choice = random.choice(list(RockPaperScissors))
        else:
            self.__inputChoice()
        
        self.__printChoice()
            
    def __printChoice(self):
        if self.choice is RockPaperScissors.rock:
            print(f"{self.name} choose Rock")
        elif self.choice is RockPaperScissors.paper:
            print(f"{self.name} choose Paper")
        elif self.choice is RockPaperScissors.scissors:
            print(f"{self.name} choose Scissors")
    
    def getValueCompareChoice(self) -> int:
        if self.choice is RockPaperScissors.rock:
            return 1
        elif self.choice is RockPaperScissors.paper:
            return 2
        elif self.choice is RockPaperScissors.scissors:
            return 3
        
    def compareWith(self, player: "Player") -> Results:
        if self.getValueCompareChoice() - player.getValueCompareChoice() == 1:
            return Results.win
        elif self.getValueCompareChoice() - player.getValueCompareChoice() == -1:
            return Results.lose
        elif self.getValueCompareChoice() - player.getValueCompareChoice() == 2:
            return Results.lose
        elif self.getValueCompareChoice() - player.getValueCompareChoice() == -2:
            return Results.win
        else:
            return Results.equal
        
player1 = Player(name="User1", isComputer=True)
player2 = Player(name="User2", isComputer=True)


def playGame():
    while True:
        player1.play()
        player2.play()
        if player1.compareWith(player2) is Results.win:
            print(f"{player1.name} win {player2.name}")
            break
        elif player1.compareWith(player2) is Results.lose:
            print(f"{player1.name} lose {player2.name}")
            break
        else:
            print(f"{player1.name} equal {player2.name}")

playGame()

# Define 3 type
# Define 2 type result (hoa, thang, thua)
# setup Player class 
     # setup
        # choice
        # name
        # can random
        # input choice
            # check type
                    # player input choice
                    # if valid
                        # call func print choice
                    # elif player input wrong
                        # print invalid data and try again
        # can check is computer
        # get choice
        # play
            # if isComputer
                # random
            # else
                # input choice
                
        # create function print choice
            # name
            # if r 
                # print choice r
            # elif p
                # print choice d
            # elif s
                # print choice s
        # get compare choice -> int
            # if r 
                # return 1
            # elif p
                # return 2
            # elif s
                # return 3

# create first player
# create second player

# create function play game
    # loop infinity
        # loop
            # first play
            # second play
        # get bolt choice and print
        # call function compare choice player


# create function compare choice first player and second player return result
    # if first.player.getComparechoice - second.player.getComparechoice == 1
        # return win
    # elif first.player.getComparechoice - second.player.getComparechoice == -1
        # return lose
    # elif first.player.getComparechoice - second.player.getComparechoice == 2
        # return lose
    # elif first.player.getComparechoice - second.player.getComparechoice == -2
        # return win
    # else 
        # return hoa
    
# -2(win) -1(lose) 0(hoa) 1(win) 2(lose)

