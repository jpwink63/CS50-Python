#guessing game

import random

def main():
    guess(get_level())

def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            number = random.randint(1, level)
            return number

        except ValueError:
            pass

def guess(number):
    while True:
        try:
            answer = int(input("Guess: ").strip())
            if answer == number:
                print("Just right!")
                break
            elif answer > number:
                print("Too large!")
            elif answer < number:
                print("Too small!")

        except ValueError:
            pass

if __name__ == "__main__":
    main()
