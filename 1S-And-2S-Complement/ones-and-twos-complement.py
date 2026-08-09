import time

print("1s and 2s Complement Calculator\n")
integer = int(input("Enter negative integer: ").replace('-',''))
bits = 8
positive_integer = integer
number_of_zeroes = 0
num_list = []

time.sleep(3)
print("\nSTEP 1. Convert Decimal to Binary: \n")
time.sleep(3)
print(f"Note: After computing for the binary, read it from bottom to top.\n")
time.sleep(3)
while integer > 0:
    remainder = integer % 2
    print(f"{integer} / 2 = {integer // 2}\tRemainder: {remainder}")
    integer //= 2
    time.sleep(1)
    num_list.append(remainder)

binary = "".join((map(str, num_list[::-1])))
print(f"\n\t > {positive_integer} (Positive Decimal) to Binary (base 2) = {binary}")


while len(num_list) < bits:
    num_list.append(0)
    number_of_zeroes +=1

base = "".join(list(map(str, num_list))[::-1])
first_complement = "".join(['1' if num == 0 else '0' for num in num_list][::-1])
second_complement = first_complement
final_answer = []

carry = 1

for number in second_complement[::-1]:
    total = int(number) + carry
    new_bit = total % 2
    carry = total // 2
    final_answer.append(new_bit)


final_answer = "".join(list(map(str, final_answer)))


time.sleep(3)
print("\nSTEP 2. Compute the base.")
print(f"\nNote: Use the binary from step 1 '{binary}' and add zeroes to the left to complete {bits} bits.")
time.sleep(3)
print(f"\n\t > Base (+{positive_integer}): {base}\t\t# We added {number_of_zeroes} zeroes on the left to complete {bits} bits.")


time.sleep(3)
print("\nSTEP 3. Compute the 1s Complement")
time.sleep(3)
print(f"\nNote: Change all 1s to 0s and 0s to 1s. flip the base: '{base}'")
time.sleep(3)
print(f"\n\t > 1s Complement (flip): {first_complement}\t\t# We change all 1s to 0s and 0s to 1s.")

time.sleep(3)
print("\nSTEP 4. Compute the 2s Complement")
time.sleep(3)
print(f"\nNote: Add 1 to the rightmost number in {first_complement}. Binary Addition.")
time.sleep(3)
print(f"\n\t > 2s Complement (+1): {final_answer[::-1]}")

time.sleep(3)
print(f"\n\n > Final Answer: {final_answer[::-1]}")





