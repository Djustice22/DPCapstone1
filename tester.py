import sqlite3
import csv

# import bcrypt
from time import gmtime, strftime

connection = sqlite3.connect("Competency_Tracking_Tool.db")
cursor = connection.cursor()

# *******************************************Employee Search Works
# employee_search = input(
#     "Type in the employee name you would like to search or press enter to view all: "
# )


# def view_all_employees(where=None):
#     if where:
#         where = f"%{where}%"
#         rows = cursor.execute(
#             "SELECT * FROM Employees Where First_Name LIKE ?", (where,)
#         ).fetchall()
#     else:
#         rows = cursor.execute("SELECT * FROM Employees").fetchall()

#     print(
#         f'{"Emp_id":10}{"First_Name":25}{"Last_Name":25}{"Phone":15}{"Email":30}{"Password":80}{"Active":15}{"Date_Created":15}{"Hire_Date":15}{"Emp_Type"}'
#     )
#     print(
#         f'{"------":10}{"----------":25}{"---------":25}{"-----":15}{"-------------":30}{"----------":80}{"------":15}{"------------":15}{"---------":15}{"--------"}'
#     )
#     for row in rows:
#         print(
#             f"{row[0]:<10}{row[1]:25}{row[2]:25}{row[3]:15}{row[4]:30}{row[5]:25}{row[6]:15}{row[7]:<15}{row[8]:15}{row[9]}"
#         )


# view_all_employees(employee_search)


# def all_competencies(where=None):
#     if where:
#         where = f"%{where}%"
#         rows = cursor.execute(
#             "SELECT * FROM Competencies WHERE Comp_Name LIKE ?",
#             (
#                 where,
#                 where,
#                 where,
#                 where,
#             ),
#         ).fetchone
#     else:
#         rows = cursor.execute("SELECT * FROM Competencies").fetchall()

#         print(
#             f'{"Comp_Id":10}{"Comp_Name":40}{"Comp_Description":40}{"Comp_Created":20}'
#         )
#         print()
#         for row in rows:
#             print(f"{row[0]:<10}{row[1]:40}{row[2]:40}{row[3]:20}")


# comp_search = input(
#     "Type in the employee name you would like to search the competencies for OR press ENTER to view all: "
# )

# all_competencies()


def add_employee():
    add_new_employee = "INSERT INTO Employees (First_Name,Last_Name,Phone,Email,Password,Active,Date_Created,Hire_Date,Emp_Type) VALUES(?,?,?,?,?,?,?,?,?)"
    fname = input("Enter first name: ").title()
    lname = input("Enter last name: ").title()
    phone = input("Enter phone number: ")
    email = input("Enter email address: ").lower()
    password = input("Enter new password: ")
    active = input("Type the number 1 for active or 0 for not active: ")
    cdate = input("Enter today's date as date file was created (M-DD-YY format): ")
    hdate = input("Enter hired date (M-DD-YY format): ")
    emp_type = input("Type out if this is an employee or manager: ").lower
    month, day, year = map(int, cdate.split and hdate.split("-"))
    date1 = datetime.date(month, day, year)

    add_emp_values = [
        fname,
        lname,
        phone,
        email,
        password,
        active,
        cdate,
        hdate,
        emp_type,
    ]
    print(add_employee())
    cursor.execute(add_new_employee, add_emp_values, date1)


connection.commit()
