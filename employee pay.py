

def calc_gross_pay(pay_rate,hours_worked):
    gross_pay=pay_rate*hours_worked
    return gross_pay
employee_pay_rate=float(input('pls enter hours pay rate: '))
employee_hours=float(input('pls enter hours worked: '))
employee_gross_pay=calc_gross_pay(employee_pay_rate, employee_hours)
print('employee gross pay is $'+ format(employee_gross_pay, '.2f'))
