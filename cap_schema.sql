 CREATE TABLE IF NOT EXISTS Empoyees (
    Emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    First_Name TEXT,
    Last_Name TEXT,
    Phone TEXT,
    Email TEXT,
    Password TEXT,
    Active INTEGER DEFAULT 1,
    Date_Created TEXT,
    Hire_Date TEXT,
    Emp_Type TEXT,
    );

CREATE TABLE IF NOT EXISTS Competencies (
    Comp_Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Comp_Name INTEGER,
    Comp_Description INTEGER,
    Comp_Created_Date TEXT,
    FOREIGN KEY (Comp_id) REFERENCES Users (User_id)
    FOREIGN KEY (Comp_id) REFERENCES Assessment (Comp_id)
    );

CREATE TABLE IF NOT EXISTS Assessment Results (
    User_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Assessment_id INTEGER,
    Score INTEGER, 
    Date_Taken TEXT,
    Manager TEXT,
    FOREIGN KEY (Manager) REFERENCES Users (User_id),
    PRIMARY KEY ()
    );

    CREATE TABLE IF NOT EXISTS Assessment_Data (
    Assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Comp_id INTEGER,
    Assessment_Name TEXT,
    Date_Created TEXT,
    Measurement TEXT,
    Interview TEXT,
    Test TEXT,
    Project TEXT,
    FOREIGN KEY (Assessment_id) REFERENCES Assessment Results (Assessment_id)
    );