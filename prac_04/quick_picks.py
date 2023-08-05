MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 45
NUMBER_PER_LINE = 6


def main():
    import random
    times_to_pick = int(input("How many quick picks? "))

    for time in range(1, times_to_pick + 1):
        random_list = []
        # get 6 different random number
        while len(random_list) < NUMBER_PER_LINE:
            random_number = random.randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
            if random_number not in random_list:
                random_list.append(random_number)
        random_list.sort()
        for number in random_list:
            print(f"{number:2}", end=" ")
        print("\n")


main()