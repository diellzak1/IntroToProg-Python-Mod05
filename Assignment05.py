# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Diellza Mehmeti,11/15/2024, Assignment05
# ------------------------------------------------------------------------------------------ #

import json
from typing import TextIO

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data:str = ''  #Holds
student_data: dict[str,str] = {}  # one row of student data
students: list = []  # a table of student data
file:TextIO = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError:
    print("File not found. Creating new file.")
    open(FILE_NAME, 'w')
except Exception as e:
    print("Unknown Exception", type(e), e, sep='\n')
finally:
    if file and not file.close:
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name.isalpha(): #adding exception if the first name contains numerical values
                raise ValueError("The first name should contain letters only.")

            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name.isalpha(): #adding exception if the first name contains numerical values
                raise ValueError("The last name should contain letters only.")

            course_name = input("Please enter the name of the course: ").strip()

            student_data = {'FirstName': student_first_name, 'LastName':student_last_name, 'CourseName':course_name}
            students.append(student_data) #add new data to the dictionary
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e:
            print(e)  # Prints the custom message


    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        except Exception as e:
            print("Error saving to file")
            print(e)
        finally:
            if file and not file.closed:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3") #prints the message if user enters any value other than 1,2,3

print("Program Ended")
