LENGTH = 5

password = input("")
while len(password) < LENGTH:
    print("Invalid length")
    password = input("")
print("*" * len(password))