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
    name = input("First Denizen, what shall we call you?\n")

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
    score = 0
    if difficulty == 1:
        answer = random.randint(1,10)
    elif difficulty == 2:
        answer = random.randint(1,50)
    else:
        answer = random.randint(1,100)
    while guess != answer:
        score += 1
        guess = int(input(f"What is your guess, {player}?\n"))
        if guess < answer:
            print(f"Your guess is too low, Denizen {player}!\n")
        elif guess > answer:
            print(f"Your guess is too high, Denizen {player}!\n")
    print(f"Congratulations Denizen {player}! You took {score} tries to reach the correct answer!\n")
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
    choice = 0
    while choice < 4 and choice > -1:
        choice = int(input("1. Play \n2. Leaderboard \n3. Settings \n4. Exit\n"))
        if choice == 1:
            difficulty = input(f"What is your difficulty level, Denizen {player}? \n1. Easy \n2. Medium\n3. Hard\n")
            score = playGame(player, difficulty)
        elif choice == 2:
            print("This feature has yet to be implemented! Return soon to see progress!")
        elif choice == 3:
            print("This feature has yet to be implemented! Return soon to see progress!")
    
    print(f"Gilbert: Poor Denizen {player}! Maybe you'll keep your world's honor next time!!!")

    return 0

#def timer():

#def saveScore():

