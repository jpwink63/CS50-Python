#game Little Professor in python

import random


def main():

    level = get_level()
    i = 0
    right = 0

    while i < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0

        while tries < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x + y):
                    tries = 4
                    i += 1
                    right += 1
                else:
                    tries += 1
                    print("EEE")

                if tries == 3:
                    print(f"{x} + {y} =", (x + y))
                    i += 1

            except Exception:
                tries += 1
                print("EEE")

                if tries == 3:
                    print(f"{x} + {y} =", (x + y))
                    i += 1

    print("Score:", right)

def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if 1 <= level <= 3:
                return level

        except ValueError:
            pass


def generate_integer(level):
    stop = 0
    start = 0
    match level:
        case 1:
            stop = 9
            start = 0
        case 2:
            stop = 99
            start = 10
        case 3:
            stop = 999
            start = 100

    return random.randint(start, stop)


if __name__ == "__main__":
    main()
