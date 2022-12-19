 CREATE TABLE IF NOT EXISTS Employees (
    Emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    First_Name TEXT,
    Last_Name TEXT,
    Phone TEXT,
    Email TEXT UNIQUE,
    Password TEXT,
    Active INTEGER DEFAULT 1,
    Date_Created TEXT,
    Hire_Date TEXT,
    Emp_Type TEXT
    );

  
 CREATE TABLE IF NOT EXISTS Competencies (
    Comp_Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Comp_Name TEXT,
    Comp_Description TEXT,
    Comp_Created_Date TEXT
    );
 
 
CREATE TABLE IF NOT EXISTS Assessment_Data (
    Assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Comp_id INTEGER,
    Assessment_Name TEXT,
    Date_Created TEXT,
    Test1_Method TEXT,
    Test1_Date TEXT,
    Test2_Method TEXT,
    Test2_Date TEXT,
    Test3_Method TEXT,
    Test3_Date TEXT,
    FOREIGN KEY (Comp_id) REFERENCES Competencies (Comp_id)
    );

CREATE TABLE IF NOT EXISTS Assessment_Results (
    User_id INTEGER,
    Assessment_id INTEGER,
    Date_Taken TEXT,
    Score INTEGER, 
    Manager TEXT,
    FOREIGN KEY (Manager) REFERENCES Users (User_id),
    FOREIGN KEY (User_id) REFERENCES Users (User_id),
    FOREIGN KEY (Assessment_id) REFERENCES Assessment_Data (Assessment_id),
    PRIMARY KEY(User_id, Assessment_id, Date_Taken)
    );