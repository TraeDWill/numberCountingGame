import classes
import random
'''
    First interaction with the user, and gets player name.

    Args:
        None

    returns:
        name: Name of the player

'''
def introduction():
    #Introduction
    print("Hello Denizen of the world of Guess. We are here to put to the test your ability to keep your world's honor!")
    print("This will be a test of you ability to guess numbers! The longer it takes, the worse of a score you will receive! Can you truly keep your world's honor?")
    name = input("First Denizen, what shall we call you?")

    return name

'''
    This is the gameplay loop function.

    Args:
        player: The name of the player
        difficulty: The difficulty the player has chosen
    
    return:
        score: This is the score the player achieved in the game
'''

def playGame(player, difficulty):
    guess = 0
    if difficulty == 1:
        answer = random.randint(1,10)
    elif difficulty == 2:
        answer = random.randint(1,50)
    else:
        answer = random.randint(1,100)
    while guess != answer:
        score += 1
        guess = input(f"What is your guess, {player}?")
        if guess < answer:
            print("Your guess is too low, Denizen {player}!")
        elif guess > answer:
            print("Your guess is too high, Denizen {player}!")
    print("Congratulations Denizen {player}! You took {score} tries to reach the correct answer!")
    return score


'''
    The user will choose between: Play, Leaderboard and Settings. This will be where the all of the gameplay functions will be used.

    Args:
        None
    
    Return:
        None
'''
def menu():
    player = introduction()
    while choice != 4:
        choice = input("1. Play \n2. Leaderboard \n3. Settings \n4. Exit\n")
        if choice == 1:
            difficulty = input("What is your difficulty level, Denizen {player}? \n1. Easy \n2. Medium\n3. Hard\n")
            score = playGame(player, difficulty)
        elif choice == 2:
            print("This feature has yet to be implemented! Return soon to see progress!")
        elif choice == 3:
            print("This feature has yet to be implemented! Return soon to see progress!")
        elif choice == 4:

    return choice

#def timer():

#def saveScore():

