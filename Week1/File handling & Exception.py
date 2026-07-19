#Write user input to file
content=input("Enter the data")
file=open("output.txt","w")
file.write(content)
file.close()
print("Data written successfully")

#Read from file
file=open("output.txt","r")
output=file.read()
print(output)
file.close()

#Word count
sentence = input("Enter a sentence: ")

if sentence.strip() == "":
    print("Number of words = 0")
else:
    words = sentence.split()
    print("Number of words =", len(words))

#Zero division handling
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#Read csv file
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)      # Skip header

    for row in reader:
        print("Name:", row[0])
        print("Age:", row[1])
        print("Marks:", row[2])
        print()