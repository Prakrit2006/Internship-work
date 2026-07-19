#Python Print function
print("Hello World")



#Addition of two number
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("a+b=",a+b)

#Square & Cube of a number
#Exponent operator
c=int(input("Enter number for cube and Square"))
print("Sqaure of",c ,"is=",c**2,"\nCube of ",c,"is=",c**3)
#using pow function
#print(pow(c,2))
#print(pow(c,3))

#Name & age formated output
Name=input("Enter Name")
Age=input("Enter Age")
print("Name",Name,"Age",Age)
print(f"Name is {Name} and Age is {Age}")
print("Formatted output")
print(f"{'Name':<20}:{Name}\n{Age:<20}:{Age}")


#Data type identification
a = 25
b = 3.5
c = "Python"
d = False
e = [1, 2, 3]
f = (1, 2, 3)
g = {1, 2, 3}
h = {"name": "John"}
i = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))