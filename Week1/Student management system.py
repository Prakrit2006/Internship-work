Student={}
import csv
try:
    with open("Student.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            Student[row[0]] = {"Roll": row[1], "Marks": row[2], "Age": row[3]}
except FileNotFoundError:
    print("No existing records found")

def add_student():
    print("-"*50)
    name = input("Enter Student Name ")
    if name in Student:
        print("Student already exists")
        return
    roll=input("Enter Roll Number ")
    marks=float(input("Enter Marks "))
    age=input("Enter Age ")
    Student[name]={"Roll":roll,"Marks":marks,"Age":age}

def display_student():
    print("-"*50)
    if len(Student)==0:
        print("No Records found")
    else:
        print("Student Records:")
        print("-"*50)
        for name,data in Student.items():
            print("Name :", name)
            print("Roll :", data["Roll"])
            print("Age :", data["Age"])
            print("Marks :", data["Marks"])
            print("----------------------")

def save_to_file():
    with open("Student.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Roll", "Marks", "Age"])
        for name,data in Student.items():
            writer.writerow([name,data["Roll"],data["Marks"],data["Age"]])


def average_marks():
    print("-"*50)
    total=0
    for data in Student.values():
        total+=float(data["Marks"])
    avg=total/len(Student.keys())
    print("Average Marks:",avg)

while  True:
    print("="*50)
    print("Welcome to Student Management System")
    print("1.Add Student")
    print("2.Display Student")
    print("3.Average Marks")
    print("4.Save to file")
    print("5.Exit")

    num=int(input("Enter the option "))
    if num==1:
        add_student()
    elif num==2:
        display_student()
    elif num==3:
        average_marks()
    elif num==4:
        save_to_file()
    elif num==5:
        break
    else:
        print("Invalid Option")
