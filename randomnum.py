import random
#import logo_art
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level):
    if level=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
def check_answer(guessed_num,answer,attempts):
    if guessed_num<answer:
        print("Your guess is too low")
        return attempts-1
    elif guessed_num>answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"Your guess is right... The answer was {answer}")
def game():
    #print(logo_art.logo)
    print("let me thick of a number between 1 to 50")
    answer=random.randint(1,50)
    print(answer)
    level=input("choose level of difficulty...type 'easy' or 'hard': ")
    attempts=set_difficulty(level)
    guessed_number=0
    while guessed_number!=answer:
        print(f"You have {attempts} remaining to guess the number.")

        guessed_number=int(input("guess a number:"))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print("you are out of guesses...you lose")
            return
        elif guessed_number!=answer:
            print("guess again")
game()