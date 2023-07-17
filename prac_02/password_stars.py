#Constant
LENGTH = 5


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """print *"""
    print("*" * len(password))


def get_password():
    """get the password"""
    password = input("")
    while len(password) < LENGTH:
        print("Invalid length")
        password = input("")
    return password


main()