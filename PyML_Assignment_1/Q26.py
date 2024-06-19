# Check string starts or ends with particular prefix or suffix
# Defining the string to be checked
str1 = "Momotaro is my favourite character."
# Checking presence of prefix : startswith method
if str1.startswith("Momo"):
    print("The string starts with the prefix")
else:
    print("The string does not start with the prefix")
# Checking presence of suffix : endswith method
if str1.endswith("."):
    print("The string ends with the suffix")
else:
    print("The string does not end with the suffix")