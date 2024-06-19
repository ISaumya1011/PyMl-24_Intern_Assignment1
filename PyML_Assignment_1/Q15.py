#Importing csv module
import csv
# Open a file with given path and read its contents
with open('C:/Users/Saumya Gupta/Downloads/anshi11.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# Displaying on console done