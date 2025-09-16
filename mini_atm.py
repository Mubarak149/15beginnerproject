# deposit
# checkbalance
# withdraw

account = 0

def deposit():
    global account
    amount = int(input("Enter Amount: "))
    account += amount
    

def checkbalance():
    print("Your Balance is:",account)
    
def withdraw():
    global account
    amount = int(input("Enter Amount to withdraw: "))
    account -= amount
    
while True:
    print("1. Deposit money to account")
    print("2. Withdraw money to account")
    print("3. Check balance")
    print("4. Quit")
    option = input("Enter option: ")
    if option == "1":
        print("You want to deposit")
        deposit()
    elif option == "2":
        print("You want to withdraw")
        withdraw()
    elif option == "3":
        print("this is your balance")
        checkbalance()
    elif option == '4':
        break
    else:
        print("invalid Choice")