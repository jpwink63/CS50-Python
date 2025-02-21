#basic calculator in python

expression = input("x, y, z: ")

x, y, z = expression.split(" ")

x = int(x)
z = int(z)

match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        result = x / z

print(f"{result:.1f}")
