# 1.
name = input("Please input your name: ")
output_file = open("name.txt", 'w')
print(f"{name}", file=output_file)
output_file.close()

# 2.
input_file = open("name.txt", 'r')
print(f"Your name is {name}")
input_file.close()

# 3.
input_file = open("numbers.txt", 'r')
first_number = input_file.readline(3)
second_number = input_file.readline(4)
x = int(first_number) + int(second_number)
print(x)

# 4.
input_file = open("numbers.txt", 'r')
for line in input_file:
    print(line.strip())