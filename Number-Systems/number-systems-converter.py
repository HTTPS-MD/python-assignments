import time

print("Base 10 to any Number System Converter")

number = int(input("Enter a number to convert: "))
number_system = int(input("Enter a number system: "))

base_numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
time.sleep(0.8)

print("\nCalculating...\n")
time.sleep(2)
converted = []

while number > 0:
    remainder = number % number_system

    print(f"{number} / {number_system} = {number // number_system} Remainder = {base_numbers[remainder]}")
    time.sleep(1)
    converted.append(base_numbers[remainder])
    number = number // number_system

print("\nRead the remainder upwards!\n")
print("Calculation Results: \n ->", "".join(map(str, converted[::-1])))