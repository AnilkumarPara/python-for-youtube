"""
Write a program for an ATM machine that allows users to withdraw cash.
The user should input the amount they want to withdraw, and the program
should deduct the amount if the user has sufficient balance.
Display an appropriate message if the withdrawal is successful
or if there are insufficient funds.
"""
# predefined account balance
account_balance = 1000
withdrawal_amount = int(input("Howmuch amount to be withdrawn"))

if withdrawal_amount > 0:
    if withdrawal_amount <= account_balance:
        print(f"Withdrawal successful. Remaining balance: {account_balance - withdrawal_amount}")
    else:
        print("Insufficient funds.")
else:
    print("Invalid withdrawal amount.")

