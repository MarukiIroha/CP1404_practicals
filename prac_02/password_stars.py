#Constant
LENGTH = 5


def main():
    password = get_password()
    print("*" * len(password))


def get_password():
    """get the password"""
    password = input("")
    while len(password) < LENGTH:
        print("Invalid length")
        password = input("")
    return password


main()