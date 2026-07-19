#Even/Odd checker
Number=int(input("Enter Number"))
if Number%2==0:
    print("Number",Number,"is even")
else:
    print("Number",Number,"is odd")

#Largest of 3 Number
print("Enter numbers in the form A B C")
a,b,c=map(int,input("Enter Number").split())
if a>=b and a>=c:
    print("Largest Number =",a)
elif b>=a and b>=c:
    print("Smallest Number =",b)
else:
    print("Largest Number =",c)

#Print 1-100
for i in range(1,101):
    print(i,end="")
print()

# Sum of N numbers
N=int(input("Enter Number N to sum N numbers"))
Sum=0
for i in range(1,N+1):
    Sum +=i
print(Sum)
# Using formula N*(N+1)//2 faster

#Multiplication table
n=int(input("Enter Number to print table of"))
print("Multiplication table of",n)
print("-"*11)
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

#Prime number check
num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime Number")
            break
    else:
        print(num, "is a Prime Number")
