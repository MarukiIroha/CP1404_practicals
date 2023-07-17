for i in range(1, 21, 2):
    print(i, end=' ')
print()
"""
loop a.
"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()
"""
loop b.
"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()
"""
loop c.
"""
stars = int(input("Number of stars: "))
for i in range(0, stars):
    print("*", end='')
print()
"""
loop d.
"""
stars = int(input("Number of stars: "))
line = 1
for i in range(0, stars):
    for j in range(0, line):
        print("*", end='')
    line = line + 1
    print()