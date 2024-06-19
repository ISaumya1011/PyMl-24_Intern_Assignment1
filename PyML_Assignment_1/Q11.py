# Take integer input as no. of sequence members
num = int(input("Enter no. of members reqd. in fibonacci series : "))
n1 = 0
n2 = 1
i=0
# Display 1st n 2nd nos.
print(n1)
print(n2)
# For loop to iterate and assign next number
for i in range(0,num-2):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3