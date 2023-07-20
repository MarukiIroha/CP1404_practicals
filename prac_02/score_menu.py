#Constant
VALID_CHOICE = 'QGPS'
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    score = 0
    print(MENU)
    choice = get_valid_choice()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result= get_result(score)
            print(result)
        else:
            print("*" * score)
        print(MENU)
        choice = get_valid_choice()
    print("Farewell")


def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def get_valid_choice():
    choice = input(">>> ").upper()
    while choice not in VALID_CHOICE:
        print("Invalid option")
        choice = input(">>> ").upper()
    return choice


def get_result(score):
    if score > 90:
        result = str("Excellent")
    elif score > 50:
        result = str("Passable")
    else:
        result = str("Bad")
    return result


main()