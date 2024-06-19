# Function to count occurrences of a specific element in a list
def count_occurrences(l1, ele):
    return l1.count(ele)
# Input the list of elements
l1_in = input("Enter elements of the list separated by spaces: ").split()
# Input the element to count
element = input("Enter the element to count: ")
# Count the occurrences of the specified element
result = count_occurrences(l1_in, element)
print("The no. of occurences of ",element," is ",result)

