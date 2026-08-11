file_name = input("Enter File Name: ")
number = int(input("0 = Directory\n1 = Python File\nEnter Choice: "))
special_symbols = '!@#$%^&*()_+={[}]|:;"<,>.?/ '



new_name = ""
for character in file_name:
    if character not in special_symbols:
        new_name += character
    else:
        new_name += "-"

if number == 0:
    print(new_name.title())

else:
    print(f"{new_name.lower()}.py")

