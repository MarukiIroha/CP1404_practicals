"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
#Constant
VALID_CHOICE = 'QCF'
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = get_valid_choice()
    while choice != "Q":
        if choice == "C":
            fahrenheit = transfer_to_fahrenheit()
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = transfer_to_celsius()
            print(f"Result: {celsius:.2f} F")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def transfer_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def transfer_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def get_valid_choice():
    choice = input(">>> ").upper()
    while choice not in VALID_CHOICE:
        print("Invalid option")
        choice = input(">>> ").upper()
    return choice


main()