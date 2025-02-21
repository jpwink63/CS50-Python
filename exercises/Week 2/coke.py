#coke machine, insert your coins

amount = 50

while True:
    print("Amount Due:", amount)
    insert = int(input("Insert Coin: "))
    if insert == 25 or insert == 10 or insert == 5:
        amount -= insert
        if amount > 0:
            continue
        else:
            print("Change Owed:", amount * -1)
            break
