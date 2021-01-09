# mortgage.py
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage.1
# The interest rate is 5% and the monthly payment is $2684.11.
# Exercise 1.7

# Exercise 1.8
# Calculate the total payment and number of months if Dave pays an extra 1000 dollars in the first 12 months

# Exercise 1.9
# Add a start and end mont for the extr payment

# Exercise 1.10
# Create a table

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0

extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    total_months += 1
    final_payment = payment

    if total_months >= extra_payment_start_month and total_months <= extra_payment_end_month:
        final_payment += extra_payment

    principal_with_raiting = principal * (1+rate/12)

    if(principal_with_raiting < final_payment):
        final_payment -= principal
        principal = 0
    else:
        principal = principal_with_raiting - final_payment

    total_paid = total_paid + final_payment
    print(
        f'Month {total_months} were paid a total of {total_paid}. Remaining: {principal}')


print('Total paid', round(total_paid, 4), 'Total months', total_months)
