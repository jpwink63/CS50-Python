#remove the vowels of a word

x = list(input("Input: "))
y = ""

for i in x[:]:
    if i.lower() in "aeiou":
        x.remove(i)

for i in x:
    y += i

print(y, end="")
