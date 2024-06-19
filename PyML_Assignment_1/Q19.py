import string
def remove_punc(str1):
    translator = str.maketrans('', '', string.punctuation)
    return str1.translate(translator)
if __name__ == "__main__":
    text = input("Enter a string: ")
    result = remove_punc(text)
    print("String without punctuation:", result)