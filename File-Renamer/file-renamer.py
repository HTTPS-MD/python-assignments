file_name = input("Enter File Name: ")

number = -1
special_symbols = '!@#$%^&*()_+={[}]|:;"<,>.?/ '

print("\n0 = Directory\n1 = Python File\n2 = Function Name\n")
while number < 0 or number > 2:
    number = int(input("Enter Choice: "))

    if number < 0 or number > 2:
        print(" > Should not be > 2 or < 0!\n")


new_name = ""
for character in file_name:
    if character not in special_symbols:
        new_name += character
    else:
        new_name += "-"


if number == 0:
    print(new_name.title())

elif number == 1:
    print(f"{new_name.lower()}.py")

elif number == 2:
    print(f"{new_name.replace('-', '_')}")

