import calculator

if __name__ == "__main__":
    bill = int(input("Input bill amount: "))
    tip = int(input("Tip Percentage? "))

    print("Your tip will be:", calculator.calculate_tip(bill, tip))