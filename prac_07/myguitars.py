import csv
from collections import namedtuple
from prac_07.guitar import Guitar


def main():
    """Read file of guitar details, save as objects, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
    guitars.sort()
    in_file.close()

    for guitar in guitars:
        print(guitar)


main()