
# define all variables
balance = 3329

monthlyPaymentRate = 0
annualInterestRate = 0.2

# calculates the minimum payment
def minimum_payment(a, b):
    """
    input: outstanding balanceance (a) and minimum payment rate (b)
    output: returns the minimum payment amount
    """
    return a*b
    
# calculates the unpaid balanceance 
def unpaid_balanceance(a,b):
    """
    input: outstanding balanceance and minimum payment amount
    output: returns the unpaid payment amount
    """
    return a -b
    
def int_pmt(a,b):
    """
    input: outstanding balanceance and minimum payment amount
    output: returns the interest paid
    """
    return a*(b/12)
 
for i in range(1,13) :
    
    var_min_pmt = minimum_payment(balance, monthlyPaymentRate)
    
    var_unpaid_balance = unpaid_balanceance(balance,var_min_pmt)
    
    var_int = int_pmt(var_unpaid_balance,annualInterestRate)
    
    balance = round(var_unpaid_balance + var_int, 2)
    
print("remaining balance is: ", balance)
    
    
    
    
    