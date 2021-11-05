import random

picked_number = random.randint(1, 999) 

def guessing_game():
    while True:
        guessednumber = int(input("pick a number between 1 and 999\n"))
        if guessednumber == picked_number:
            print("You found the number. Congratulations!")
            return False
        elif guessednumber < picked_number:
            print("increase your number")
        elif guessednumber > picked_number:
            print("decrease your number")
guessing_game()