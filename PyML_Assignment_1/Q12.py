#Taking input of no. whose digits to be added
#Taking string input for easy iteration of digits
num = input("Enter the no. whose digits to be added : ")
sum = 0  #Initialising sum variable to store sum
#Iterate along digits using for loop
for i in num:
    sum = sum + int(i)
#Displaying output
print("The sum is : ",sum)