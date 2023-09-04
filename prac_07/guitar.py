"""
programming language
Estimate: 30 minutes
Actual:   22 minutes
"""
CURRENT_YEAR = 2023
VINTAGE_YEAR = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : {self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def __iter__(self):
        return iter([self.name, self.year, self.cost])