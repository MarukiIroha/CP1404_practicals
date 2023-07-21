"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
# TODO: Fix this!

def main():
    score = float(input("Enter score: "))
    result_input = get_result(score)
    choice = random.randint(1, 100)
    result_random = get_result(choice)
    print(result_input)
    print(result_random)


def get_result(score):
    if score < 0 or score > 100:
        result = str("Invalid score")
    else:
        if score > 90:
            result = str("Excellent")
        elif score > 50:
            result = str("Passable")
        else:
            result = str("Bad")
    return result


main()