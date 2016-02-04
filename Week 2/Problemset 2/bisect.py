
new_balance = balance
Monthly_interest_rate = (annualInterestRate) / 12
Montly_Lower = balance / 12
epsilon = 0.01
Montly_Upper = (balance * (1 + Monthly_interest_rate) ** 12) / 12
month_pay = (Montly_Upper + Montly_Lower) / 2.0

while abs(new_balance) >= epsilon:
    new_balance = balance
    for i in range(0, 12):
        new_balance = round(
            ((new_balance - month_pay) * (1 + Monthly_interest_rate)), 2)
        if new_balance >= 0:
            Montly_Lower = month_pay
        else:
            Montly_Upper = month_pay
            month_pay = (
                Montly_Upper + Montly_Lower) / 2.0
            print('Lowest Payment:: ' +
              str(round(month_pay, 2)))
