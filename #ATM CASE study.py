#ATM CASE study
balance = 50000
print('ATM menu')
print('1.create account')
print('2.Deposite')
print('3.Withdraw')
print('4.check balance')
print('5. Exit')
choice=int(input('enter your choice from menu'))
if choice == 1:
    name = input("Enter your name: ")
    balance = float(input("Enter initial deposit: "))
    account_created = True
    print("Account created successfully!")
    print("Welcome", name)
elif choice ==2:
    amount = float(input('enter amount to deposite'))
    balance = amount + balance
    print("deposite successful")
    print("updated balance",balance)
elif choice ==3:
    amount = float(input('enter amount to withdraw'))

    if amount <= balance:
        balance = balance - amount
        print("withdraw successful")
        print("remaining balance =", balance)
    else:
        print("Insufficient Balance")

elif choice == 4:
    print("Remaining Balance",balance)

else:
    print("Invalid Choice")