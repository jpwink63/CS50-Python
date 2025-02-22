#make your grocery list

list = {}

while True:
    try:
        item = input().strip().lower()
        if item:
            list[item] = list.get(item, 0) + 1

    except EOFError:
        print("\n")
        break

for i in sorted(list):
    print(f"{list[i]} {i.upper()}")
