########## MANAGER ADD ASSESSMENTS #6
def add_assess():
    insert_querya = "INSERT INTO Assessment_Data (Assessment_id, Comp_id, Assessment_Name, Date_Created) VALUES(?,?,?,?)"
    assess_name = input("Enter the new assessment name: ")
    assess_create = input("Enter today's date: ")
    new_assess_values = [assess_name, assess_create]
    cursor.execute(insert_querya, new_assess_values)


########## MANAGER ADD ASSESSMENT RESULTS #7
def new_assess_results():
    insert_queryr = "INSERT INTO Assessment_Results (User_id, Assessment_id, Date_Taken, Score, Manager) VALUES(?,?,?,?,?)"
    comp_input = input("Enter competency name: ")
    comp_input_date = input("Enter today's date")
    assess_results_values = [insert_queryr, comp_input, comp_input_date]
    cursor.execute(insert_queryr, assess_results_values)


########## MANAGER ADD COMPETENCY #8
def add_comp():
    insert_query = "INSERT INTO Competencies (Comp_Name, Comp_Description,Comp_Created) VALUES(?,?,?)"
    comp_name = input("Enter the new compentency name: ")
    comp_desc = input("Enter the new compentency description: ")
    comp_create = input("Enter today's date: ")
    new_comp_values = [comp_name, comp_desc, comp_create]
    cursor.execute(insert_query, new_comp_values)
    connection.commit()


########## EDIT/ADD COMPETENCIES

########## EDIT/ADD ASSESSMENTS

########## EDIT/ADD ASSESSMENT RESULTS

########## EMPLOYEE COMPETENCY SUMMARY REPORT
def comp_summary_report():
    pass


########## COMPETENCY RESULTS SUMMARY REPORT
def comp_results_report():
    pass
