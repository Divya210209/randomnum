import random
lower_bound=1
upper_bound=100
max_attempts=5
target_number=random.randint(lower_bound, upper_bound)

for attempts in range(max_attempts):
    guess=int(input(f"guess the number between {lower_bound} and {upper_bound}: "))
    if guess<target_number:
        print("Too low!")
    elif guess>target_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number!")
        break