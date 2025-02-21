#identifies whether the greeting begins with hello, h or not

greeting = input("What they said? ").strip().lower()

match greeting:
    case hello if hello.startswith("hello"):
        print("$0")
    case h if h.startswith("h"):
        print("$20")
    case _:
        print("$100")
