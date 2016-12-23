# Credit card details.
balance = 320000
annualInterestRate  = 0.2
monthlyInterestRate = annualInterestRate/12.0

PMT_lower = balance/12
PMT_upper = (balance*(1 + monthlyInterestRate)**12)/12
monthlyPayment = (PMT_upper - PMT_lower)/2
threshold = 0.01

# Calculate the minimum fixed monthly payment.
payOffBalance = False

while (not payOffBalance):
    debt = balance
    monthlyPayment = (PMT_upper + PMT_lower)/2
    
    # For each month.
    for month in range(1,13):    
        # Update the outstanding debt.
        monUnpaidBalance = debt - monthlyPayment
        debt = (monUnpaidBalance * monthlyInterestRate) + monUnpaidBalance
    
    # Is the debt paid?
    if ((debt >=0) and (debt <= threshold)):
        payOffBalance = True
    elif (debt > threshold):
        PMT_lower = monthlyPayment
    elif (debt < 0):
        PMT_upper = monthlyPayment
    
# Print out the result statement with the lowest payment.
print('Lowest Payment: ', round(monthlyPayment,2))