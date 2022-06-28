loan_amt = float(input('Enter the loan amount: '))
loan_rate = float(input('Enter the interest rate in % : '))
loan_duration = int(input('Enter the loan duration (in months): '))

r = (loan_rate / 100) / 12


formula = (r*(1+r)**loan_duration) / ((1+r)**loan_duration -1)
M = loan_amt
monthly_payment = M * formula


print('Your monthly payment for your mortgage is', monthly_payment)
