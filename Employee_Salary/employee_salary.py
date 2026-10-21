def employee_salary(hworked : int, hrate : int) -> int:

    regularPay = hrate * hworked

    if (hworked > 40):
        overtime = ((hworked - 40) * 1.5) * hrate
        regularPay = (hworked - (hworked - 40)) * hrate

    grossSalary = regularPay + overtime
    deduction = grossSalary * 0.05
    netSalary = grossSalary - deduction

    return f"\nREGULAR PAY: P{regularPay}\nOVERTIME PAY: P{overtime}\nGROSS SALARY: P{grossSalary}\nDEDUCTION (5%): P{deduction}\nNET SALARY: P{netSalary}"



if __name__ == "__main__":
    hoursWorked = int(input("Hours Worked: "))
    hourlyRate = int(input("Hourly Rate: "))

    print(employee_salary(hoursWorked, hourlyRate))