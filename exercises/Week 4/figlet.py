#using FIGlet library

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():
    format = get_font()
    figlet.setFont(font = format)
    text = get_text()
    print("Output:", figlet.renderText(text))


def get_font():
    fonts = figlet.getFonts()
    font = sys.argv[-1]
    check = sys.argv[1]
    try:
        if font in fonts:
            if check == "-f" or check == "--font":
                return font
        else:
            sys.exit

    except IndexError:
        return random.choice(fonts)

def get_text():
    while True:
        try:
            text = input("Input: ").strip()
            return text

        except ValueError:
            pass


if __name__ == "__main__":
    main()
