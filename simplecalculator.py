user_number = float(input("Enter your first number: "))
user_number2 = float(input("Enter your second number: "))
user_operator = input("Enter you operator(+, -, *, /): ")

if user_number and user_number2:
    if user_operator == '+':
        print(user_number + user_number2)
    elif user_operator == '-':
        print(user_number - user_number2)
    elif user_operator == '*':
        print(user_number * user_number2)
    elif user_operator == '/':
        print(user_number / user_number2)
    else:
        print("Sorry you didnt put an operator")
    
else:
    print(' you didnt put number')
