# mortgage.py
#Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage.1
# The interest rate is 5% and the monthly payment is $2684.11.
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0

while principal > 0:
    total_months += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', round(total_paid,4), 'Total months', total_months)