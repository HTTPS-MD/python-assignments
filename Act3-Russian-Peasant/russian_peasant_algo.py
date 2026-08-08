import os, time

header = "P-M1: Act 3: Russian Peasant Algorithm (RPA) Implementation\nProgrammed by: Francisco, Mark Daniel B.\n=========================================================="
print(header)

print("\nINPUT")
multiplicand = int(input(" > Input Multiplicand: "))
multiplier = int(input(" > Input Multiplier: "))

addList = []

input("\nPress ENTER to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

print(header)
print("\nPROCESS")
print(f"{multiplicand} x {multiplier}\n")

while multiplicand >= 1:

    if multiplicand % 2 != 0:
        print(f"{multiplicand}   {multiplier} <<")
        addList.append(multiplier)

    else:
        print(f"{multiplicand}   {multiplier}")

    time.sleep(0.5)
    multiplicand = multiplicand // 2
    multiplier = multiplier * 2

print("\nFINAL ANSWER")
print(" + ".join(str(n) for n in addList))
print(f" = {sum(addList)}")




