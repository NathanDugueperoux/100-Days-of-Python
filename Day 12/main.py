import random

EASY = 10
HARD = 5
number = random.randint(1, 100)

print("Im thinking of a number between 1 and 100.")
start = input("Pick a difficulty. Type \"easy\" or \"hard\": ").lower()
if start == "easy":
    for i in range(EASY):
        print(f"You have {5-i} attempts left to find the number.")
        guess = int(input("Make a guess?: "))
        if guess == number:
            print(f"Well done, the number was indeed {number}")
            break
        elif guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
    print(f"The number was {number}")
elif start == "hard":
    for i in range(HARD):
        print(f"You have {5-i} attempts left to find the number.")
        guess = int(input("Make a guess?: "))
        if guess == number:
            print(f"Well done, the number was indeed {number}.")
            break
        elif guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
    print(f"The number was {number}.")
