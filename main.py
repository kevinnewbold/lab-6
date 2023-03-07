def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")


def encode(password):
    string = str(password)
    encoded = ""
    for c in string:
        encoded += str((int(c) + 3) % 10)
    return int(encoded)


def decode(password):
    decoded = password
    return decoded


def main():
    password = 0
    while True:
        print_menu()
        option = int(input("Please enter an option: "))
        print(end="\n")
        if option == 1:
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print(f"The encoded password is {password} and the original password is {decode(password)}")
        elif option == 3:
            break





if __name__ == "__main__":
    main()