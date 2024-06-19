# Taking string as input : 
str1 = input("Enter the string : ")
# Taking substring to be looked up : 
sub_str = input("Enter the substring to be searched : ")
# Using if - else to check presence of sub_str in str1
if (sub_str in str1):
    print("Yes. It's present.")
else:
    print("No. It's not present.")