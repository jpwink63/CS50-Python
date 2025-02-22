#gives adieu for you and your friends

import inflect
p = inflect.engine()

x = []

while True:
    try:
        x.append(input("Name: "))

    except EOFError:
        names = p.join(x)
        print(f"Adieu, adieu, to {names}")
        break
