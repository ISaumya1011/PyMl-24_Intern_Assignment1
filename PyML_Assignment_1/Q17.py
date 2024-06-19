'''str1 = input("Enter string to be converted to title case: ")
result = str1.title()
print(result)''' # easy approach
# alternate approach
str1 = input("Enter string to be converted to title case: ")
words = str1.split()
title_case_words = [word.capitalize() for word in words]
result = ' '.join(title_case_words)
print(result)