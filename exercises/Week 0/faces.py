#replaces :) and :( with emojis

def main():
    text = input()
    print(convert(text))

def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x

main()
