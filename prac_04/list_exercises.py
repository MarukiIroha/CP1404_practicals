# 1.
MAXIMUM_NUMBER = 5


def main():
    numbers = []

    for number in range(1, MAXIMUM_NUMBER + 1):
        number = int(input("Number: "))
        numbers.append(number)

    print_number(numbers)


def print_number(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers)/MAXIMUM_NUMBER}")


main()

# 2.
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Please input your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")