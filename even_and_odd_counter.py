user_input = input("Enter Your Numbers with comma: ")
string_numbers = user_input.split(',') #['1', '2', '3', '4', '5', '6', '7']
even = []
odd = []
for string_number in string_numbers:
    int_number = int(string_number)
    if int_number % 2 == 0:
        even.append(int_number)
    else:
        odd.append(int_number)
    
print("even numbers:",even)
print("odd numbers:", odd)