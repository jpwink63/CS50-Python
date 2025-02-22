#format dates in ISO 8601 standard

list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if "," in date:
            month, day, year = date.split(" ")
            month = list.index(month) + 1
            day = int(day.replace(",", ""))
            if (1 <= month <= 12 and 1 <= day <= 31):
                print(f"{year}-{month:02}-{day:02}")
                break

        else:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            if (1 <= month <= 12 and 1 <= day <= 31):
                print(f"{year}-{month:02}-{day:02}")
                break

    except ValueError:
        pass
