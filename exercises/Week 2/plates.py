#check if a vanity plate is valid

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[:2].isalpha():
            has_number = False
            for i in range(len(s)):
                if s[i].isdigit():
                    if s[i] == "0" and not has_number:
                        return False
                    has_number = True
                elif has_number:
                    return False
            return s.isalnum()


main()
