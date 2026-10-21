def employee_salary(hworked: float, hrate: float) -> str:
    overtime = 0.0

    if hworked > 40:
        overtime = (hworked - 40) * 1.5 * hrate
        regular_pay = 40 * hrate
    else:
        regular_pay = hworked * hrate

    gross_salary = regular_pay + overtime
    deduction = gross_salary * 0.05
    net_salary = gross_salary - deduction

    return (
        f"\nREGULAR PAY: P{regular_pay:,.2f}"
        f"\nOVERTIME PAY: P{overtime:,.2f}"
        f"\nGROSS SALARY: P{gross_salary:,.2f}"
        f"\nDEDUCTION (5%): P{deduction:,.2f}"
        f"\nNET SALARY: P{net_salary:,.2f}"
    )


if __name__ == "__main__":
    hours_worked = float(input("Hours Worked: "))
    hourly_rate = float(input("Hourly Rate: "))

    print(employee_salary(hours_worked, hourly_rate))