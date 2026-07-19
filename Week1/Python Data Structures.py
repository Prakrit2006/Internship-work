#Sum of list elements
List=list(map(int,input("Enter List").split()))
Sum=0
for i in List:
    Sum+=i
print(Sum)

#Max & Min in list
#Python has built in function for said task max() & min()
#Using for loop
List1=list(map(int,input("Enter List").split()))
Max=List1[0]
Min=List1[0]
for i in List1:
    if i>Max:
        Max=i
    if i<Min:
        Min=i
print("Maximum of list is",Max,"Minimum of list is",Min)

#Sort list(ASC/DESC)
numbers = list(map(int, input("Enter numbers: ").split()))

numbers.sort()

print("Ascending Order:", numbers)

numbers.sort(reverse=True)

print("Descending Order:", numbers)

#Frequency counter
Number=[1,1,1,2,2,3,4,2,1,3,4]
Freq={}
for i in Number:
    Freq[i]=Freq.get(i,0)+1
for key, value in Freq.items():
    print(key, "appears", value, "times")

#Student marks dictionary
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78}

for name, marks in student_marks.items():
    print(name, ":", marks)
n = int(input("Enter number of students to be inserted: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    student_marks[name] = marks

print(student_marks)

highest_name = ""
highest_marks = 0

for name, marks in student_marks.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_name = name

print("Highest Scorer:", highest_name)
print("Marks:", highest_marks)
