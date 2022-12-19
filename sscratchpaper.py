import sqlite3
import csv

connection = sqlite3.connect("Practice.db")
cursor = connection.cursor()


def insert_schema():
    with open("scomps.sql", "rt") as insert_queries:
        queries = insert_queries.read()
        cursor.executescript(queries)

    connection.commit()


insert_schema()

# from datetime import datetime

# def get_date_string():
#     right_now = datetime.now()
#     return right_now.strftime(%Y-%m-%d %H:%M:%S)

# insert_query = "INSERT INTO Employees (Emp_Id,First_Name,Last_Name,Phone,Email,Password,Active,Date_Created,Hire_Date,Emp_Type) VALUES (?,?,?,?,?,?,?,?,?)"
# # insert_values = (
#     Emp_Id,
#     First_Name,
#     Last_Name,
#     Phone,
#     Email,
#     Password,
#     Active,
#     Hire_Date,
#     Emp_Type,
# )


# def insert_courses_schema():
#     with open("courses_insert_data.sql", "rt") as insert_queries:
#         queries = insert_queries.read()
#         cursor.executescript(queries)

#     # connection.commit()


# # insert_courses_schema()


# def insert_cohorts_schema():
#     with open("cohorts_insert_data.sql", "rt") as insert_queries:
#         queries = insert_queries.read()
#         cursor.executescript(queries)


# #     connection.commit()


# # insert_cohorts_schema()


# def insert_registration_schema():
#     with open("registration_insert_data.sql", "rt") as insert_queries:
#         queries = insert_queries.read()
#         cursor.executescript(queries)


#     connection.commit()


# insert_registration_schema()


# def view_all_employees():
#     all_query = "SELECT * Emp_id, First_Name, Last_Name, Phone, Email, Password, Active, Date_Created, Hire_Date, Emp_Type FROM Employees"
#     rows = cursor.execute(all_query)
#     rows = rows.fetchall()

#     print(
#         f'{"Emp_id":10}{"First_Name":25}{"Last_Name":25}{"Phone":15}{"Email":30}{"Password":25}{"Active":15}{"Date_Created":15}{"Hire_Date":15}{"Emp_Type"}'
#     )
#     print(
#         f'{"------":10}{"----------":25}{"---------":25}{"-----":15}{"-------------":30}{"----------":25}{"------":15}{"------------":15}{"---------":15}{"--------"}'
#     )
#     for row in rows:
#         print(
#             f"{row[0]:<10}{row[1]:25}{row[2]:25}{row[3]:15}{row[4]:30}{row[5]:25}{row[6]:15}{row[7]:<15}{row[8]:15}{row[9]}"
#         )


# view_all_employees()
