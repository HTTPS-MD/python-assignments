import time

print("\nMost Significant Bit Calculator\n")

binary = []
bits = 16
integer = int(input("\nEnter an integer: "))
positive_integer = abs(integer)
positive = integer > 0

integer = positive_integer

print(f"\n+{integer} (Base 10) to Binary Calculations: \n")
time.sleep(2)

while integer > 0:
    remainder = integer % 2
    print(f"{integer} / 2 =  {integer // 2}\tRemainder = {remainder}")
    time.sleep(1)
    integer //= 2
    binary.append(remainder)


binary = list(map(str, binary))[::-1]


while len(binary) < bits:
    binary.insert(0, "0")

changed_sign = binary.copy()
changed_sign[0] = "0" if positive else "1"


binary_str = "".join(binary)
changed_sign_str = "".join(changed_sign)

time.sleep(1)
print(f"\nBase (+{positive_integer}): {binary_str}")
time.sleep(1)
print(f"Sign Magnitude (-{positive_integer}): {changed_sign_str}")