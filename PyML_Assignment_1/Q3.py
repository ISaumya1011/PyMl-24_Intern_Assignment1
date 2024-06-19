# Taking input of number a whose factorial to be calculated
a = int(input("Enter the number : "))
# Initiating fact variable to store answer
fact = 1
# Defining for loop to iterate n do repititive multiplication
for i in range(1,a+1):
    fact = fact*i
# Displaying output
print("Factorial of given no. ",a," is : ",fact)