def atm_withdrawal(balance, amount):
    if amount > balance:
        return "Insufficient Funds", balance
    elif amount <= 0:
        return "Invalid Amount", balance
    else: 
        balance -= amount
        return "Transaction Successful", balance