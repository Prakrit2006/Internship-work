# Student Management System
## Description
The Student Management System is a python based console program that allows user to manage student records efficiently. It uses python dictonaries and csv file handling to handle and permanently store student information

## Features

- Load Student data from a CSV file
- Add new student records
- Display student records
- Calculate Average marks of all students
- Save student records to a CSV file
- Console menu interface

## Technologies used

- Python 3
- CSV modules
- Dictionaries
- Functions
- File handling

---
## Project Structure

```
Student Management System/
│
├── main.py          # Main Python program
├── Student.csv      # Stores student records
└── README.md        # Project documentation
```

---
## Student Record Format

Each student record contains:

- Name
- Roll Number
- Marks
- Age

## Functionalities

### 1. Add Student

Allows the user to enter:

- Student Name
- Roll Number
- Marks
- Age

The information is stored in a dictionary.

---

### 2. Display Students

Displays all student records in a readable format.

---

### 3. Average Marks

Calculates the average marks of all students stored in the dictionary.

---

### 4. Save to File

Saves all student records into `Student.csv`.

---

### 5. Exit

Terminates the application.

---