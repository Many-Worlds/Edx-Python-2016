# Paste your code into this box
balance = 20000        
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
Monthly_interest = annualInterestRate / 12
Month= 1
paid = 0

for num in range(0,12,1):
    Minimum_month_pay = monthlyPaymentRate  * balance
    balance -= Minimum_month_pay
    balance *= Monthly_interest + 1
    print('Month: ' + str(Month))
    print('Minimum monthly payment: '+ str(round(Minimum_month_pay,2)))
    print('Remaining balance:: '+str(round(balance,2)))
    Month += 1
    paid += Minimum_month_pay
    print('Total paid: '+ str(round(paid,2)))
    print('Remaining balance: '+ str(round(balance,2)))
