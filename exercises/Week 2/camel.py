#CamelCase

x = list(input("Input: "))
y = ""

for i in x[:]:
    if not i.isupper():
        y += i
    else:
        y += "_"
        y += i.lower()

print(y)
