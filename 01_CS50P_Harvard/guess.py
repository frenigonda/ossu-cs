import random

def get_guess():
    random_value = random.randint(1, 100)
    guess = 0
    while random_value != guess:
        guess = int(input("Enter a guess between 1 and 100: "))
        if guess == random_value:
            print("You've guessed correctly!")
        elif guess > random_value:
            print("Nope! Try a smaller value")
        else:
            print("Oh no! Try a bigger number")


get_guess()