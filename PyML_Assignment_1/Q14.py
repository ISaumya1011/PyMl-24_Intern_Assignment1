def read_lines_until_empty():
    lines = []
    print("Enter multiple lines of input (press Enter on empty line to finish n display):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    print("\nOutput:")
    for line in lines:
        print(line)
# Call the function to execute the program
read_lines_until_empty()
# Confirmation printing
print("Done printing!!")