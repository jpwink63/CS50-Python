#check for meal time

def main():
    clock = input("What's the time? ")
    decimal_time = convert(clock)

    if 7 <= decimal_time <= 8:
        print("breakfast time")
    elif 12 <= decimal_time <= 13:
        print("lunch time")
    elif 18 <= decimal_time <= 19:
        print("dinner time")

def convert(time):
    hour, minutes = time.split(":")
    hour = int(hour)
    minutes = int(minutes)
    return float(hour + (minutes/60))

if __name__ == "__main__":
    main()
