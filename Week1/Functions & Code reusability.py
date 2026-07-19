#Factorial Function
def Factorial(n):
    if n==0:
        return 1
    else:
        return n*Factorial(n-1)
print(Factorial(int(input("Enter a Number for factorial: "))))

#Palindrone checker
def is_palindrome(value):
    return value == value[::-1]

text = input("Enter a string: ")

print("Palindrome" if is_palindrome(text) else "Not a Palindrome")

# Calculator using functions
def calculator(a, b, operator):

    if operator == '+':
        return a + b

    elif operator == '-':
        return a - b

    elif operator == '*':
        return a * b

    elif operator == '/':
        return a / b

    else:
        return "Invalid operator"


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

print("Result =", calculator(a, b, op))

#Lambda square function
square = lambda x: x * x
num = int(input("Enter a number: "))
print("Square =", square(num))

#Average of list function
def average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


numbers = [10, 20, 30, 40, 50]
print("Average =", average(numbers))