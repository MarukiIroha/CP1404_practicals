import csv
from collections import namedtuple
from prac_07.guitar import Guitar


def main():
    """Read file of guitar details, save as objects, display."""
    guitars = []

    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: $")
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "added.")
        name = input("Name: ")

    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
    guitars.sort()
    in_file.close()

    for guitar in guitars:
        print(guitar)

    with open("guitars.csv", "w", newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(guitars)
    out_file.close()

main()