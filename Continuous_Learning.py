import sqlite3
import csv

# import bcrypt
from time import gmtime, strftime
import datetime

connection = sqlite3.connect("Competency_Tracking_Tool.db")
cursor = connection.cursor()


########## CURRENT TIME with hours, mins, seconds
# print("----------------------------------------")
# s = strftime("%c")
# print("Date and Time of login:", s)
# print()

# ########## WELCOME MANAGER HEADER
# mwelcome = "*****Welcome to the Student App Manager Menu*****\n"
# print(mwelcome)
# print("----------------------------------------")

# ########## WELCOME EMPLOYEE HEADER
# ewelcome = "*****Welcome to the Student App Employee Menu*****\n"
# print(ewelcome)
# print("-------------------------------------")


########### LOGIN HEADER
def login():
    print("Please log in to the Competency Tracking Tool to begin: \n")
    email = input("Enter your email: ")
    passcode = input("Enter your password: ")
    password, emp_type = cursor.execute(
        "SELECT Password,Emp_Type FROM Employees WHERE email=?", (email,)
    ).fetchone()
    if bcrypt.checkpw(passcode.encode(), password.encode()) == True:
        if emp_type == "Manager":
            manager_menu(emp_type)
        else:
            employee_menu(emp_type)
    else:
        print("Invalid Login")


# login()

# connection.commit

########## MANAGER MENU
def manager_menu():
    while True:
        print()
        m_menu = input(
            """Hello, (persons name), Choose from the following options: \n
        1. View all employees
        2. View Competencies for ALL employees
        3. View Assessments for ALL Employees
        4. Search Employee
        5. Add new employee
        6. Add new assessment to competencies
        7. Add new assessment result for employee
        8. Add Competency
        9. Make Edits
        >>>"""
        )
        if m_menu == "1":
            view_all_employees()
        elif m_menu == "2":
            pass
        elif m_menu == "3":
            pass
        elif m_menu == "4":
            pass
        elif m_menu == "5":
            pass
        elif m_menu == "6":
            pass
        elif m_menu == "7":
            pass
        elif m_menu == "8":
            pass
        elif m_menu == "9":
            pass
        else:
            print("You did not make a valid selection.")


manager_menu()


########## EMPLOYEE MENU
def employee_menu():
    while True:
        print()
        e_menu = print(
            """Hello, Choose from the following options: \n
        1. View my user information
        2. View my Competencies
        3. View my Assessments and Results
        4. Update my personal information
        >>>"""
        )

        if e_menu == "1":
                view_all_employees()
            elif e_menu == "2":
                pass
            elif e_menu == "3":
                pass
            elif e_menu == "4":
                pass
    # employee_menu()


########## VIEW ALL EMPLOYEES OR SEARCH FOR EMPLOYEE HEADERS #1
def view_all_employees(search=None):
    if search:
        search = f"%{search}%"
        rows = cursor.execute(
            "SELECT * FROM Employees Where name LIKE ?", (search,)
        ).fetchall()
    else:
        rows = cursor.execute("SELECT * FROM Employees").fetchall()

    print(
        f'{"Emp_id":10}{"First_Name":25}{"Last_Name":25}{"Phone":15}{"Email":30}{"Password":25}{"Active":15}{"Date_Created":15}{"Hire_Date":15}{"Emp_Type"}'
    )
    print(
        f'{"------":10}{"----------":25}{"---------":25}{"-----":15}{"-------------":30}{"----------":25}{"------":15}{"------------":15}{"---------":15}{"--------"}'
    )
    for row in rows:
        print(
            f"{row[0]:<10}{row[1]:25}{row[2]:25}{row[3]:15}{row[4]:30}{row[5]:25}{row[6]:15}{row[7]:<15}{row[8]:15}{row[9]}"
        )
    view_all_employees()


########## FOR EMPLOYEES TO VIEW THEIR OWN INFORMATION
def emploee_record():
    emp_search = input("")
    my_search = cursor.execute("SELECT * FROM Employees Where name LIKE ?").fetchone()


emploee_record(view_all_employees)

########## MANAGER VIEW EMPLOYEES AND THEIR COMPETENCIES OR A SINGLE EMPLOYEE #2 and #4
def all_competencies():
    if where:
        where = f"%{where}%"
        rows = cursor.execute(
            "SELECT * FROM Competencies WHERE Comp_Name LIKE ?",
            (
                where,
                where,
                where,
            ),
        ).fetchall
    else:
        rows = cursor.execute("SELECT * FROM Competencies").fetchall()

        print(
            f'{"Comp_Id":10}{"Comp_Name":20}{"Comp_Description":40}{"Comp_Created":20}'
        )
        for row in rows:
            print(f"{row[0]:<10}{row[1]:20}{row[2]:40}{row[3]:20}")

    comp_search = input(
        "Type in the employee name you would like to search the competencies for OR press ENTER to view all: "
    )

    all_competencies(comp_search)


########## MANAGER VIEW ALL EMPLOYEE ASSESSMENTS #3
def all_assessments():
    if where:
        where = f"%{where}%"
        rows = cursor.execute(
            "SELECT * FROM Assessment_Data WHERE Assessment_Name LIKE ?",
            (
                where,
                where,
                where,
                where,
            ),
        ).fetchall
    else:
        rows = cursor.execute("SELECT * FROM Assessment_Data").fetchall()

        print(
            f'{"Assessment_id":8}{"Comp_id":8}{"Assessment_Name":40}{"Date_Created":15}'
        )
        for row in rows:
            print(f"{row[0]:<8}{row[1]:8}{row[2]:40}{row[3]:15}")

    comp_search = input(
        "Type in the employee name you would like to search the assessments for OR press ENTER to view all: "
    )


########## FOR MANAGER TO ADD NEW EMPLOYEE #5
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

    cursor.execute(add_new_employee, add_emp_values, date1)





########## MANAGER EDIT/UPDATE EMPLOYEE INFORMATION #9
def employee_update():
    headers = [
        "First_Name",
        "Last_Name",
        "Phone",
        "Email",
        "Password",
        "Active",
        "Date_Created",
        "Hire_Date",
        "Emp_Type",
    ]

    emp_to_edit = input(
        "Enter the name of the employee you want to update information on: \n"
    )
    view_all_employees(emp_to_edit)

    user_id = input("What employee ID do you want to update? ")

    print("Please pick an option to update:")
    for index, item in enumerate(headers, start=1):
        print(f"{index}: {item}")

    user_input = input(">>> ")
    user_choice = headers[int(user_input) - 1]

    update_choice = headers[user_choice]

    emp_update_query = f"UPDATE Employees SET {update_choice} = ? WHERE emp_id = ?"
    new_update = input(f"New {update_choice} has been added: ")

    values = new_update

    cursor.execute(emp_update_query, values)
    connection.commit()


employee_update()
connection.commit()


# ##########CREATED THE CONTINUOUS LEARNING TABLE######
def insert_schema():
    with open("cap_schema_copy.sql", "rt") as insert_queries:
        queries = insert_queries.read()
        cursor.executescript(queries)


#     connection.commit()


# insert_schema()


# ##########ADDED CSV DATA FOR FOUR TABLES:
def import_csv_users():  #                0         1      2     3      4        5      6            7          8
    query = "INSERT INTO Employees (First_Name,Last_Name,Phone,Email,Password,Active,Date_Created,Hire_Date,Emp_Type) VALUES (?,?,?,?,?,?,?,?,?)"
    with open("list_employees_copy.csv", "rt") as csv_query:
        reader = csv.reader(csv_query)
        fields = next(reader)
        for row in reader:
            first_name = row[0]
            last_name = row[1]
            phone = row[2]
            email = row[3]
            password = row[4]
            active = row[5]
            date_created = row[6]
            hire_date = row[7]
            emp_type = row[8]

            hashed_password = bcrypt.hashpw(
                password.encode(), salt=bcrypt.gensalt()
            ).decode()

            csv_data = [
                first_name,
                last_name,
                phone,
                email,
                hashed_password,
                active,
                date_created,
                hire_date,
                emp_type,
            ]
            cursor.execute(query, csv_data)


#         connection.commit()


# import_csv_users()

def export_csv():
    with open ('export_results.csv', 'w') as my_csv:
        writer = csv.writer()
        writer.writerows()

def import_csv_comps():
    query = "INSERT INTO Competencies (Comp_name,Comp_Description,Comp_Created_Date) VALUES (?,?,?)"
    with open("list_comps.csv", "rt") as csv_query:
        reader = csv.reader(csv_query)
        csv_data = []
        fields = next(reader)
        for row in reader:
            csv_data.append(row)
    for record in csv_data:

        cursor.execute(query, record)


#     connection.commit()


# import_csv_comps()


def import_csv_data_assess():
    query = "INSERT INTO Assessment_Data (Assessment_Name,Date_Created,Test1_Method,Test1_Date,Test2_Method,Test2_Date,Test3_Method,Test3_Date) VALUES (?,?,?,?,?,?,?,?)"
    with open("list_data_assess.csv", "rt") as csv_query:
        reader = csv.reader(csv_query)
        csv_data = []
        fields = next(reader)
        for row in reader:
            csv_data.append(row)
    for record in csv_data:

        cursor.execute(query, record)


#     connection.commit()


# import_csv_data_assess()


def import_csv_data_resutls():
    query = "INSERT INTO Assessment_Results (Date_Taken,Score,Manager) VALUES (?,?,?)"
    with open("list_results_assess.csv", "rt") as csv_query:
        reader = csv.reader(csv_query)
        csv_data = []
        fields = next(reader)
        for row in reader:
            csv_data.append(row)
    for record in csv_data:

        cursor.execute(query, record)


#     connection.commit()


# import_csv_data_resutls()


# print()
