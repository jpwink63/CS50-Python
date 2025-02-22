#check the fuel tank level

while True:
    try:
        x, y = input("Fraction: ").split("/")
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            if y != 0 and x <= y:
                break

    except ValueError:
        pass

fuel = x/y * 100

if fuel <= 1:
    print("E")
elif fuel >= 99:
    print("F")
else:
    print("{:.0f}%".format(fuel), end="")
