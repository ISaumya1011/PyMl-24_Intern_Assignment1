# Simple Calculator with +,-,*,/ operators
print("SIMPLE CALCULATOR")
# Taking input of 2 nos. and operators
a = int(input("Enter the first no. : "))
b = int(input("Enter the second no. : "))
op_choice = input("Enter the operator you want to use (+,-,*,/) : ")
# Performing operation using if-else conditional statements
if (op_choice == '+'):
    result = a+b
elif (op_choice == '-'):
    result = a-b
elif (op_choice == '*'):
    result = a*b
elif (op_choice == '/'):
    result = a/b
else:
    result = "not defined. Enter a valid operator!"
# Displaying output
print("The result is ",result)