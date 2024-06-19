# Taking string as input : 
str1 = input("Enter the string : ")
# Writing it to a file with given path
file = "D://Internships//Python ML Internship//PyMl_1.txt"
f = open(file,'w') # write mode
f.write(str1)
# Confirmation printing
print("Done!!")