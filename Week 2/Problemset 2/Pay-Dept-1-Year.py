Monthly_interest = annualInterestRate / 12

min_payment = 0
new_balance = balance
while new_balance >= 0:
    new_balance = balance
            min_payment += 10
                for month in range(0, 12, 1):
                    new_balance -= min_payment
                                    new_balance *= (1 +
                                                    (annualInterestRate / 12))
                                    print("Lowest payment: " +
                                          str(min_payment))
