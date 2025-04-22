"""
Write a program that simulates rolling a pair of dice. Each time the program runs, it
should randomly generate two numbers between 1 and 6 (inclusive), representing
the result of each die. The program should then display the results and ask if the
user would like to roll again.

Optional Enhancements
• Modify the program so the user can specify how many dice they want to roll.
• Add a feature that keeps track of how many times the user has rolled the dice
during the session. This will require a counter that increments each time the
dice are rolled. 
"""

import random

def rollDiceGame():
    
    def start() -> bool:
        isRollAuto = input("Do you want roll automation? {y/N}: ").lower() == "y"
        isRollManually = True
        currentIndex = 0
        timesInput = 0
        
        if isRollAuto:
            isRollManually = False
            try:
                timesInput = int(input("How many times you want to roll dive? "))
            except ValueError:
                print("input number, please")
                start()

        while isRollManually or currentIndex < timesInput:
            if isRollManually:
                isRollManually = input("Roll the dice? y/N: ").lower() == "y"
                
            leftDice = int(random.randint(a = 1, b = 6))
            rightDice = int(random.randint(a = 1, b = 6))
            print(f"({leftDice}, {rightDice})")
            currentIndex += 1

    start()
    print("Good bye")
    
rollDiceGame()