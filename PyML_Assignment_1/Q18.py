def are_anagrams(str1, str2):
    # Removing spaces and convert to lowercase for a case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Checking if sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)
word1 = "Silent"
word2 = "Listen"
if are_anagrams(word1, word2):
    print("Words '",word1,"' and '",word2,"' are anagrams.")
else:
    print("Words '",word1,"' and '",word2,"' are not anagrams.")
