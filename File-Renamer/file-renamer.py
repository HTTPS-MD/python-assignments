file_name = input("Enter File Name: ")
number = int(input("0 = Directory\n1 = Python File\nEnter Choice: "))



if number == 0:
    print(file_name.replace(" ", "-").title())

else:
    print(file_name.replace(" ", "-").lower()+".py")