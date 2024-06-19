# Reading a file from given path
file_r = "D://Internships//Python ML Internship//PyMl_1.txt"
f = open(file_r,'r') # read mode
str1 = f.readlines()
print(str1) # printing contents of the file
# Confirmation printing
print("Done reading!!")
# Writing it to a file with given path
file_w = "D://Internships//Python ML Internship//PyMl_2.txt"
f = open(file_w,'w') # write mode
f.writelines(str1)
# Confirmation printing
print("Done writing!!")