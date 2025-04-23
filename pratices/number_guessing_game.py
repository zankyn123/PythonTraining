"""
Write a program to have the computer randomly select a number between 1 and
100, and then prompt the player to guess the number. The program should give
hints if the guess is too high or too low.

Optional Enhancements
• Allow the user to specify the minimum and maximum values for the number
range before the game starts. This gives the player more control over the
difficulty level.
• Implement a feature that limits the number of guesses a player can make. If
the player runs out of attempts, the game should end, and the correct number
should be revealed.
• Add a feature that keeps track of the fewest attempts it took to guess the
number correctly. The program should display this "best score" at the end of
each game.
"""


# start game
    
    # create number user input guess mininum
    # create number user input guess maximum
        # user input a number minimum
        # if not number
        #   print invalid data and repeat input a number mininum
        # user input a number maximum
        # if not number
        #   print invalid data
    # create a random number in range minimum -> maximum
    # user input a max attempts
        # if not number
        #   print invalid data 
    # loop infinity:
        # if until try attempts of user greather than or equal max attempts
        #   print correct number randdom
        #   input "Failed, do you want try again ? {y/n}"
        #       if user input y:
        #           reset current attempts
        #           continue loop
        #       else:
        #           terminate
        # else
            # try
                # allow user input a number
                # if user guessing number == number of score:
                #   print congratulations and attempts
                #   call function writing scores and return list score
                #   sort values of list scores
                #   print "top attemp is {first item}"
                #   terminate
                # elif user input >= maximum
                #   print too high
                #   attempts += 1
                # elif user input < maximum/2
                #   print too low
                #   attempts += 1
        
# writing scores and return list score
    # handling exception
        # open files number of score
        # writing current score into files
        # reading files
        # return list score

import random

def startGame():
    minimumNumberGuess = 0
    maximumNumberGuess = 0    
    
    while True:
        try:
            minimumNumberGuess = int(input("Input minimum number of guess: "))
            break
        except ValueError:
            print("Invalid minimum number of guess, try again")
    
    while True:
        try:
            maximumNumberGuess = int(input("Input maximum number of guess: "))
            break
        except ValueError:
            print("Invalid minimum number of guess, try again")
    
    numberRandom = random.randint(minimumNumberGuess, maximumNumberGuess)
    maxAttempts = 0
    currentAttempt = 0
    
    while True:
        try:
            maxAttempts = int(input("Input maximum of attempt: "))
            break
        except ValueError:
            print("Invalid maximum of attempt, try again")
            
    while True:
        if currentAttempt >= maxAttempts:
            try:
                choice = str(input(f"Game over!\nRandom number is {numberRandom},\nDo you want try again ? (y/n): ")).lower()
                if choice == "y":
                    currentAttempt = 0
                    continue
                else:
                    break
            except ValueError:
                print("Invalid maximum of attempt, try again")
        else:
            try:
                guessNumber = int(input(f"Guess the number(btw {minimumNumberGuess} to {maximumNumberGuess}): "))
                if guessNumber == numberRandom:
                    print(f"Congratulations, You guessed the number in {currentAttempt}")
                    break
                elif guessNumber <= round(maximumNumberGuess / 2):
                    print("Try again, too low")
                    currentAttempt += 1
                else:
                    print("Try again, too high")
                    currentAttempt += 1
                
            except ValueError:
                print("Invalid maximum of attempt, try again")


startGame()
    
    
    
        


    