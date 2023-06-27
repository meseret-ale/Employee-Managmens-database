# Author: Meseret Alemnew Melese

from os import system
import re
# importing mysql connector
import mysql.connector

# Establish a connection to the MySQL server
con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="EmployeeDB"
)

# Functions to add elements in all tables
def add_Dependent():
    print("{:>60}".format("-->>Add DEPENDENT Record<<--"))
    NAME = input("ENTER DEPENDENT NAME: ")
    if (check_DEPENDENT_NAME(NAME) == True):
        print("Dependent Name is Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        add_Dependent()
    EID = input("ENTER EMPLOYEE ID: ")
    if EID == "":
        EID = None
    elif check_employee(EID) == False:
        print("EMPLOYEE ID DOSEN'T Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        menu()
    birth_date = input("ENTER Birth Date: ")
    relationship = input("enter relationship: ")
    sex = input("enter sex: ")
    data = (NAME, birth_date,  relationship, sex, EID)
    sql = 'insert into dependent values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Successfully Added dependent Record")
    press = input("Press Any Key To Continue..")
    menu()
  
def Add_Employ():
    print("{:>60}".format("-->>Add Employee Record<<--"))
    EId = input("Enter Employee Id: ")
    if (check_employee(EId) == True):
        print("Employee ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    JTId = input("Enter JOB TITLE NAME: ")
    if JTId == "":
        JTId = None
    elif (check_job_title(JTId) == False):
        print("JOB TITLE ID DOSEN'T Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        menu()

    SId = input("Enter supervisor Id: ")
    if SId == "":
        SId = None
    
    elif check_supervisor(SId) == False:
        print("supervisor ID DOSEN'T Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        menu()
    Name = input("Enter Employee Name: ")
    MNAME = input("Enter Employee Middle Name: ")
    LNAME = input("Enter Employee Last Name: ")
    birth_day = input("Enter Employee birth day: ")
    Address = input("Enter Employee Address: ")
    Salary = input("Enter Employee Salary: ")
    sex = input("Enter Employee sex: ")
    data = (EId, birth_day,  Name, MNAME, LNAME, sex,  Salary, Address,  SId, JTId)
    sql = 'insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key To Continue..")
    menu()

def add_job_title():
    print("{:>60}".format("-->>Add JOB_TITLE Record<<--"))
    JTID = input("ENTER JOB_TITLE NAME: ")
    if (check_job_title(JTID) == True):
        print("JOB_TITLE ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        add_job_title()
    MAX_SALARY = input("ENTER THE MAX SALARY: ")
    MIN_SALARY = input("ENTER THE MIN SALARY: ")
    data = (JTID, MIN_SALARY, MAX_SALARY)
    sql = 'insert into job_titles values(%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Successfully Added job_title Record")
    press = input("Press Any Key To Continue..")
    menu()

def add_Department():
    print("{:>60}".format("-->>Add DEPARTMENT Record<<--"))
    DID = input("ENTER DEPARTMENT NAME: ")
    if (check_DEPARTMENT(DID) == True):
        print("DEPARTMENT ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        add_Department()
    EID = input("ENTER EMPLOYEE ID: ")
    if EID == "":
        EID = None
    elif check_employee(EID) == False:
        print("EMPLOYEE ID DOSEN'T Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        menu()
    LOCATION = input("ENTER LOCATION: ")
    cursor = con.cursor()
    cursor.execute('SELECT COUNT(*) FROM department')
    no_of_employee = cursor.fetchone()[0]
    start_date = input("enter the start_date: ")
    data = (DID, no_of_employee, LOCATION, start_date, EID)
    sql = 'insert into department values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Successfully Added department Record")
    press = input("Press Any Key To Continue..")
    menu()

def add_Attendance():
    print("{:>60}".format("-->>Add ATTENDANCE Record<<--"))
    AID = input("ENTER ATTENDANCE ID: ")
    if (check_Attendance(AID) == True):
        print("ATTENDANCE ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        add_Attendance()
    attendance_date = input("ENTER Atttendance Date: ")
    check_in_time = input("ENTER THE check in time: ")
    check_out_time = input("ENTER THE check out time: ")
    EID = input("ENTER EMPLOYEE ID: ")
    if (check_employee(EID) == False):
        print("EMPLOYEE ID DOESN'T Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        menu()
    data = (AID, attendance_date, check_in_time,  check_out_time, EID)
    sql = 'insert into attendance values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Successfully Added Attendance Record")
    press = input("Press Any Key To Continue..")
    menu()

def add_works():
    print("{:>60}".format("-->>Add WORKS Record<<--"))
    PID = input("ENTER PROJECT ID: ")
    if (check_PROJECT(PID) == False):
        print("PROJECT ID DOSEN'T Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        menu()
    EID = input("ENTER EMPLOYEE ID: ")
    if (check_employee(EID) == False):
        print("DPARTMENT ID DOSEN'T Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        menu()

    if PID == EID:
        print("PROJECT ID AND EMPLOYEE ID ARE THE SAME\nTry again...")
        press = input("Press Any Key To Continue..")
        menu()

    HOURS = input("ENTER HOURS: ")
    START_DATE = input("ENTER START DATE: ")
    data = (EID, PID, HOURS, START_DATE)
    sql = 'insert into works values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Successfully Added works Record")
    press = input("Press Any Key To Continue..")
    menu()

def add_Project():
    print("{:>60}".format("-->>Add PROJECT Record<<--"))
    PID = input("ENTER PROJECT Name: ")
    if (check_PROJECT(PID) == True):
        print("PROJECT ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        add_Project()
    BUDGET = input("ENTER BUDGET: ")
    location = input("Enter location: ")
    DID = input("ENTER DPARTMENT ID: ")
    if DID == "":
        DID = None
    elif check_DEPARTMENT(DID) == False:
        print("DPARTMENT ID DOSEN'T Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        add_Project()
    data = (PID, BUDGET ,location ,DID)
    sql = 'insert into project values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Successfully Added project Record")
    press = input("Press Any Key To Continue..")
    menu()
  
def check_supervisor(supervisor_id):
    sql = 'select * from employee where Supervisor_ID=%s'
    c = con.cursor(buffered=True)
    data = (supervisor_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r >= 1:
        return True
    else:
        return False
  
def check_PROJECT(PROJECT_id):
    sql = 'select * from project where project_name=%s'
    c = con.cursor(buffered=True)
    data = (PROJECT_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r >= 1:
        return True
    else:
        return False
  
def check_PROJECT_D(PROJECT_id):
    sql = 'select * from project where department_name=%s'
    c = con.cursor(buffered=True)
    data = (PROJECT_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r >= 1:
        return True
    else:
        return False
  
def check_work_e(E_id):
    sql = 'select * from works where EMPLOYEE_ID=%s'
    c = con.cursor(buffered=True)
    data = (E_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r >= 1:
        return True
    else:
        return False
   
def check_work_p(P_id):
    sql = 'select * from works where project_ID=%s'
    c = con.cursor(buffered=True)
    data = (P_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r >= 1:
        return True
    else:
        return False
    
def check_PROJECT_NAME(project_name):
    sql = 'select * from project where name=%s'
    c = con.cursor(buffered=True)
    data = (project_name,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def check_DEPENDENT_E(Dependent_id):
    sql = 'select * from dependent where EMPLOYEE_ID=%s'
    c = con.cursor(buffered=True)
    data = (Dependent_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r >= 1:
        return True
    else:
        return False
    
def check_DEPENDENT_NAME(employee_name):
    sql = 'select * from dependent where dependent_name=%s'
    c = con.cursor(buffered=True)
    data = (employee_name,)
    c.execute(sql, data)
    r = c.rowcount
    if r >= 1:
        return True
    else:
        return False
    
def check_DEPARTMENT(department_id):
    sql = 'select * from department where department_name=%s'
    c = con.cursor(buffered=True)
    data = (department_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r >= 1:
        return True
    else:
        return False
    
def check_DEPARTMENT_E(department_id):
    sql = 'select * from department where EMPLOYEE_ID=%s'
    c = con.cursor(buffered=True)
    data = (department_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r >= 1:
        return True
    else:
        return False
    
def check_Attendance(Attendance_id):
    sql = 'select * from attendance where attendance_ID=%s'
    c = con.cursor(buffered=True)
    data = (Attendance_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
 
def check_Attendance_E(Attendance_id):
    sql = 'select * from attendance where EMPLOYEE_ID=%s'
    c = con.cursor(buffered=True)
    data = (Attendance_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r >= 1:
        return True
    else:
        return False
 
def check_employee(employee_id):
    sql = 'select * from employee where EMPLOYEE_ID=%s'
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def check_employee_job(employee_id):
    sql = 'select * from employee where JOB_TITLE_ID=%s'
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r >= 1:
        return True
    else:
        return False

def check_job_title(job_title_id):
    sql = 'select * from job_titles where JOB_TITLE_ID=%s'
    c = con.cursor(buffered=True)
    data = (job_title_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r >= 1:
        return True
    else:
        return False
 
# Functions to Display contents of all tables
def Display_Employ():
    print("{:>60}".format("-->> Display Employee Record <<--"))
    sql = 'select * from employee'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee birth date: ", i[1])
        print("Employee first name: ", i[2])
        print("Employee middle name.: ", i[3])
        print("Employee last name.: ", i[4])
        print("Employee sex: ", i[5])
        print("Employee Salary: ", i[6])
        print("Employee Address: ", i[7])
        print("Employee supervisor_ID: ", i[8])
        print("Employee JOB_TITLE_ID: ", i[9])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()

def Display_Attendance():
    print("{:>60}".format("-->> Display Employee Attendance Record <<--"))
    sql = 'select * from attendance'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Attendance Id: ", i[0])
        print("Attendance date: ", i[1])
        print("check in time: ", i[2])
        print("check out time: ", i[3])
        print("Employee Id: ", i[4])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()

def Display_Department():
    print("{:>60}".format("-->> Display Departments Record <<--"))
    sql = 'select * from department'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Department Id: ", i[0])
        print("number of employee: ", i[1])
        print("location: ", i[2])
        print("name: ", i[3])
        print("start date: ", i[4])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()

def Display_dependent():
    print("{:>60}".format("-->> Display Dependent Record <<--"))
    sql = 'select * from dependent'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("dependent Id: ", i[0])
        print("birth date: ", i[1])
        print("name: ", i[2])
        print("relationship: ", i[3])
        print("sex: ", i[4])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()

def Display_job_titles():
    print("{:>60}".format("-->> Display job titles Record <<--"))
    sql = 'select * from job_titles'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("job title Id: ", i[0])
        print("job title: ", i[1])
        print("min salary: ", i[2])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()

def Display_project():
    print("{:>60}".format("-->> Display project Record <<--"))
    sql = 'select * from project'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("\n")
        print("project Name: ", i[0])
        print("budget: ", i[1])
        print("location: ", i[2])
        print("department Id: ", i[3])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()

def Display_works():
    print("{:>60}".format("-->> Display works Record <<--"))
    sql = 'select * from works'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("project Id: ", i[1])
        print("hours: ", i[2])
        print("start date: ", i[3])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()

# Functions to Update values of all tables
def Update_Employ():
    print("{:>60}".format("-->> Update Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        Update_Employ()
    else:
        Address = input("Update Employee Address: ")
        Salary = input("Update Employee Salary: ")
        sex = input("Update Employee sex: ")
        sql = 'UPDATE employee set sex = %s, salary = %s, Addres = %s where employee_id = %s'
        data = (sex, Salary, Address, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Employee Record")
        press = input("Press Any Key To Continue..")
        menu()

def Update_attendance():
    print("{:>60}".format("-->> Update Attendance Record <<--\n"))
    Id = input("Enter Attendace Id: ")
    if(check_Attendance(Id) == False):
        print("Attendace Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        Update_attendance()
    else:
        attendance_date = input("Update Atttendance Date: ")
        check_in_time = input("Update THE check in time: ")
        check_out_time = input("Update THE check out time: ")
        sql = 'UPDATE attendance set attendance_date = %s, check_in_time = %s, check_out_time = %s where attendance_ID = %s'
        data = (attendance_date, check_in_time, check_out_time, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Attendance Record")
        press = input("Press Any Key To Continue..")
        menu()

def Update_Department():
    print("{:>60}".format("-->> Update Department Record <<--\n"))
    Id = input("Enter Department Name: ")
    # checking If Employee Id is Exit Or Not
    if(check_DEPARTMENT(Id) == False):
        print("Department Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        Update_Department()
    else:
        LOCATION = input("Update LOCATION: ")
        start_date = input("Update the start date: ")
        sql = 'UPDATE department set location = %s, start_date = %s where department_name = %s'
        data = (LOCATION , start_date, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Department Record")
        press = input("Press Any Key To Continue..")
        menu()

def Update_dependent():
    print("{:>60}".format("-->> Update Dependent Record <<--\n"))
    Id = input("Enter Dependent Name: ")
    if(check_DEPENDENT_NAME(Id) == False):
        print("Dependent Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        Update_dependent()
    else:
        birth_date = input("Update Birth Date: ")
        relationship = input("Update relationship: ")
        sex = input("Update sex: ")
        sql = 'UPDATE dependent set birth_date = %s, relationship = %s, sex = %s where dependent_name = %s'
        data = (birth_date , relationship, sex, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Dependent Record")
        press = input("Press Any Key To Continue..")
        menu()

def Update_job_titles():
    print("{:>60}".format("-->> Update Job Titles Record <<--\n"))
    Id = input("Enter job_title Name: ")
    if(check_job_title(Id) == False):
        print("Job Titles Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        Update_job_titles()
    else:
        MAX_SALARY = input("Update THE MAX SALARY: ")
        MIN_SALARY = input("Update THE MIN SALARY: ")
        sql = 'UPDATE job_titles set max_salary = %s, min_salary = %s where JOB_TITLE_ID = %s'
        data = (MAX_SALARY, MIN_SALARY, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated JOB TITLE Record")
        press = input("Press Any Key To Continue..")
        menu()

def Update_Project():
    print("{:>60}".format("-->> Update Project Record <<--\n"))
    Id = input("Enter Project Name: ")
    if(check_PROJECT(Id) == False):
        print("Project Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        Update_Project()
    else:
        BUDGET = input("Update BUDGET: ")
        location = input("Update location: ")
        sql = 'UPDATE project set location = %s, budget = %s where project_name = %s'
        data = (BUDGET, location, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Project Record")
        press = input("Press Any Key To Continue..")
        menu()

def Update_Works():
    print("{:>60}".format("-->> Update Works Record <<--\n"))
    Id = input("Enter Employee Id: ")
    if(check_employee(Id) == False):
        print("Works Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()

    else:
        HOURS = input("Update HOURS: ")
        START_DATE = input("Update START DATE: ")
        sql = 'UPDATE works set hours = %s, start_date = %s where EMPLOYEE_ID = %s'
        data = (HOURS, START_DATE, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated works Record")
        press = input("Press Any Key To Continue..")
        menu()

# Functions to Promote values all tables
def Promote_Employ():
    print("{:>60}".format("-->> Promote Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Amount  = int(input("Enter Increase Salary: "))
        sql = 'select Salary from employee where EMPLOYEE_ID=%s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchone()
        t = r[0]+Amount
        sql = 'update employee set Salary = %s where EMPLOYEE_ID = %s'
        d = (t, Id)
        c.execute(sql, d)
        con.commit()
        print("Employee Promoted")
        press = input("Press Any key To Continue..")
        menu()

def Promote_Job_titles():
    print("{:>60}".format("-->> Promote Job Title Record <<--\n"))
    Id = input("Enter Job Title Id: ")
    if(check_job_title(Id) == False):
        print("Job title Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Amount  = int(input("Enter Increase Salary: "))
        sql = 'select min_salary, max_salary from job_titles where JOB_TITLE_ID=%s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchone()
        MIN_SALARY = r[0]+Amount
        MAX_SALARY = r[1]+Amount
        sql = 'update job_titles set min_salary = %s, max_salary = %s where JOB_TITLE_ID = %s'
        d = (MIN_SALARY ,MAX_SALARY , Id)
        c.execute(sql, d)
        con.commit()
        print("Job Title Promoted")
        press = input("Press Any key To Continue..")
        menu()

def Promote_Project():
    print("{:>60}".format("-->> Promote Project Record <<--\n"))
    Id = input("Enter Project Id: ")
    if(check_PROJECT(Id) == False):
        print("Project Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Amount  = int(input("Enter Increase budget: "))
        sql = 'select budget from project where project_name=%s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchone()
        t = r[0]+Amount
        sql = 'update project set budget = %s where project_name = %s'
        d = (t, Id)
        c.execute(sql, d)
        con.commit()
        print("Project Promoted")
        press = input("Press Any key To Continue..")
        menu()

# Functions to Remove all tables
def Remove_Employ():
    print("{:>60}".format("-->> Remove Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()

    else:
        if(check_Attendance_E(Id) == True):
            sql = 'delete from attendance where EMPLOYEE_ID = %s'
            data = (Id,)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()

        if(check_work_e(Id) == True):
            sql = 'delete from works where EMPLOYEE_ID = %s'
            data = (Id,)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            
        if(check_DEPENDENT_E(Id) == True):        
            sql = 'UPDATE dependent set employee_id = %s where employee_id = %s'
            data = (None, Id)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            
        if(check_DEPARTMENT_E(Id) == True):      
            sql = 'UPDATE department set employee_id = %s where employee_id = %s'
            data = (None, Id)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            
        sql = 'delete from employee where EMPLOYEE_ID = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Employee Removed")
        press = input("Press Any key To Continue..")
        menu()

def Remove_Attendance():
    print("{:>60}".format("-->> Remove Attendance Record <<--\n"))
    Id = input("Enter Attendance Id: ")
    if(check_Attendance(Id) == False):
        print("Attendance Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()

    else:
        sql = 'delete from attendance where attendance_ID = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Attendance Removed")
        press = input("Press Any key To Continue..")
        menu()

def Remove_Department():
    print("{:>60}".format("-->> Remove Department Record <<--\n"))
    Id = input("Enter Department Name: ")
    if(check_DEPARTMENT(Id) == False):
        print("Department Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    
    else:
        if(check_PROJECT_D(Id) == True):      
            sql = 'UPDATE project set department_name = %s where department_name = %s'
            data = (None, Id)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()

        sql = 'delete from department where department_name = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Department Removed")
        press = input("Press Any key To Continue..")
        menu()

def Remove_Dependent():
    print("{:>60}".format("-->> Remove Dependent Record <<--\n"))
    Id = input("Enter Dependent Id: ")
    if(check_DEPENDENT_NAME(Id) == False):
        print("Dependent Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()

    else:
        sql = 'delete from dependent where dependent_name = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Dependent Removed")
        press = input("Press Any key To Continue..")
        menu()

def Remove_job_titles():
    print("{:>60}".format("-->> Remove Job Title Record <<--\n"))
    Id = input("Enter Job Titles Id: ")
    if(check_job_title(Id) == False):
        print("Job Title Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()

    else:
        if check_employee_job(id):        
            sql = 'UPDATE employee set JOB_TITLE_ID = %s where JOB_TITLE_ID = %s'
            data = (None, Id)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()

        sql = 'delete from job_titles where JOB_TITLE_ID = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Job Title Removed")
        press = input("Press Any key To Continue..")
        menu()

def Remove_Project():
    print("{:>60}".format("-->> Remove Project Record <<--\n"))
    Id = input("Enter Project Id: ")
    if(check_PROJECT(Id) == False):
        print("Project Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()

    else:
        if(check_work_e(Id) == True):
            sql = 'delete from works where project_name = %s'
            data = (Id,)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
        sql = 'delete from project where project_name = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Project Removed")
        press = input("Press Any key To Continue..")
        menu()

def Remove_works():
    print("{:>60}".format("-->> Remove Works Record <<--\n"))
    Id = input("Enter Works Id: ")
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    PID = input("ENTER PROJECT Name: ")
    if (check_PROJECT(PID) == False):
        print("PROJECT Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()

    else:
        sql = 'DELETE FROM works WHERE EMPLOYEE_ID = %s AND project_name = %s'
        data = (Id, PID)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Works Removed")
        press = input("Press Any key To Continue..")
        menu()
         
# Functions to Search all tables
def Search_Employ():
    print("{:>60}".format("-->> Search Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()

    else:
        sql = 'select * from employee where EMPLOYEE_ID = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("\n")
            print("Employee Id: ", i[0])
            print("Employee birth date: ", i[1])
            print("Employee first name: ", i[2])
            print("Employee middle name.: ", i[3])
            print("Employee last name.: ", i[4])
            print("Employee sex: ", i[5])
            print("Employee Salary: ", i[6])
            print("Employee Address: ", i[7])
            print("Employee supervisor_ID: ", i[8])
            print("Employee JOB_TITLE_ID: ", i[9])
            print("\n")
        press = input("Press Any key To Continue..")
        menu()

def Search_Attendance():
    print("{:>60}".format("-->> Search Attendance Record <<--\n"))
    Id = input("Enter Attendance Id: ")
    if(check_Attendance(Id) == False):
        print("Attendance Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()

    else:
        sql = 'select * from attendance where attendance_ID = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("\n")
            print("Attendance Id: ", i[0])
            print("Attendance date: ", i[1])
            print("check in time: ", i[2])
            print("check out time: ", i[3])
            print("Employee Id: ", i[4])
            print("\n")
        press = input("Press Any key To Continue..")
        menu()

def Search_department():
    print("{:>60}".format("-->> Search Department Record <<--\n"))
    Id = input("Enter Department Id: ")
    if(check_DEPARTMENT(Id) == False):
        print("Department Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()

    else:
        sql = 'select * from department where department_name = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("\n")
            print("Department Name: ", i[0])
            print("number of employee: ", i[1])
            print("location: ", i[2])
            print("start date: ", i[3])
            print("employee Id: ", i[4])
            print("\n")
        press = input("Press Any key To Continue..")
        menu()

def Search_dependent():
    print("{:>60}".format("-->> Search Dependent Record <<--\n"))
    Id = input("Enter Dependent Name: ")
    if(check_DEPENDENT_NAME(Id) == False):
        print("Dependent Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()

    else:
        sql = 'select * from dependent where dependent_name = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("dependent Name: ", i[0])
            print("birth date: ", i[1])
            print("name: ", i[2])
            print("relationship: ", i[3])
            print("sex: ", i[4])
            print("employee Id: ", i[5])
            print("\n")
        press = input("Press Any key To Continue..")
        menu()

def Search_job_title():
    print("{:>60}".format("-->> Search Job Title Record <<--\n"))
    Id = input("Enter Job Title Name: ")
    if(check_job_title(Id) == False):
        print("Job Title Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()

    else:
        sql = 'select * from job_titles where JOB_TITLE_ID = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("\n")
            print("job title Name: ", i[0])
            print("min salary: ", i[1])
            print("max salary: ", i[2])
            print("\n")
        press = input("Press Any key To Continue..")
        menu()

def Search_project():
    print("{:>60}".format("-->> Search Project Record <<--\n"))
    Id = input("Enter Project Id: ")
    if(check_PROJECT(Id) == False):
        print("Project Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()

    else:
        sql = 'select * from project where project_name = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("\n")
            print("project Name: ", i[0])
            print("budget: ", i[1])
            print("location: ", i[2])
            print("department Id: ", i[3])
            print("\n")
        press = input("Press Any key To Continue..")
        menu()

def Search_works():
    print("{:>60}".format("-->> Search Works Record <<--\n"))
    Id = input("Enter Employee Id: ")
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        sql = 'select * from works where EMPLOYEE_ID = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("\n")
            print("Employee Id: ", i[0])
            print("project Id: ", i[1])
            print("hours: ", i[2])
            print("start date: ", i[3])
            print("\n")
        press = input("Press Any key To Continue..")
        menu()

#Functions to controll all tables
def employeeTable():
    print("{:>60}".format("-->> EMPLOYEE TABLE <<--")) 
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    print("{:>66}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        Add_Employ()
    elif ch == 2:
        system("cls")
        Display_Employ()
    elif ch == 3:
        system("cls")
        Update_Employ()
    elif ch == 4:
        system("cls")
        Promote_Employ()
    elif ch == 5:
        system("cls")
        Remove_Employ()
    elif ch == 6:
        system("cls")
        Search_Employ()
    elif ch == 7:
        system("cls")
        print("{:>60}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()

def attendanceTable():
    print("{:>60}".format("-->> ATTENDANCE TABLE <<--")) 
    print("1. Add ATTENDANCE")
    print("2. Display ATTENDANCE Record")
    print("3. Update ATTENDANCE Record")
    print("4. Remove ATTENDANCE Record")
    print("5. Search ATTENDANCE Record")
    print("6. Exit\n")
    print("{:>66}".format("-->> Choice Options: [1/2/3/4/5/6] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        add_Attendance()
    elif ch == 2:
        system("cls")
        Display_Attendance()
    elif ch == 3:
        system("cls")
        Update_attendance()
    elif ch == 4:
        system("cls")
        Remove_Attendance()
    elif ch == 5:
        system("cls")
        Search_Attendance()
    elif ch == 6:
        system("cls")
        print("{:>60}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()

def departmentTable():
    print("{:>60}".format("-->> DEPARTMENT TABLE <<--")) 
    print("1. Add DEPARTMENT")
    print("2. Display DEPARTMENT Record")
    print("3. Update DEPARTMENT Record")
    print("4. Remove DEPARTMENT Record")
    print("5. Search DEPARTMENT Record")
    print("6. Exit\n")
    print("{:>66}".format("-->> Choice Options: [1/2/3/4/5/6] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        add_Department()
    elif ch == 2:
        system("cls")
        Display_Department()
    elif ch == 3:
        system("cls")
        Update_Department()
    elif ch == 4:
        system("cls")
        Remove_Department()
    elif ch == 5:
        system("cls")
        Search_department()
    elif ch == 6:
        system("cls")
        print("{:>60}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()

def dependentTable():
    print("{:>60}".format("-->> DEPENDENT TABLE <<--")) 
    print("1. Add DEPENDENT")
    print("2. Display DEPENDENT Record")
    print("3. Update DEPENDENT Record")
    print("4. Remove DEPENDENT Record")
    print("5. Search DEPENDENT Record")
    print("6. Exit\n")
    print("{:>66}".format("-->> Choice Options: [1/2/3/4/5/6] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        add_Dependent()
    elif ch == 2:
        system("cls")
        Display_dependent()
    elif ch == 3:
        system("cls")
        Update_dependent()
    elif ch == 4:
        system("cls")
        Remove_Dependent()
    elif ch == 5:
        system("cls")
        Search_dependent()
    elif ch == 6:
        system("cls")
        print("{:>60}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()

def jobtitleTable():
    print("{:>60}".format("-->> JOB_TITLE TABLE <<--")) 
    print("1. Add JOB_TITLE")
    print("2. Display JOB_TITLE Record")
    print("3. Update JOB_TITLE Record")
    print("4. Promote JOB_TITLE Record")
    print("5. Remove JOB_TITLE Record")
    print("6. Search JOB_TITLE Record")
    print("7. Exit\n")
    print("{:>66}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        add_job_title()
    elif ch == 2:
        system("cls")
        Display_job_titles()
    elif ch == 3:
        system("cls")
        Update_job_titles()
    elif ch == 4:
        system("cls")
        Promote_Job_titles()
    elif ch == 5:
        system("cls")
        Remove_job_titles()
    elif ch == 6:
        system("cls")
        Search_job_title()
    elif ch == 7:
        system("cls")
        print("{:>60}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()

def projectTable():
    print("{:>60}".format("-->> PROJECT TABLE <<--")) 
    print("1. Add PROJECT")
    print("2. Display PROJECT Record")
    print("3. Update PROJECT Record")
    print("4. Promote PROJECT Record")
    print("5. Remove PROJECT Record")
    print("6. Search PROJECT Record")
    print("7. Exit\n")
    print("{:>66}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        add_Project()
    elif ch == 2:
        system("cls")
        Display_project()
    elif ch == 3:
        system("cls")
        Update_Project()
    elif ch == 4:
        system("cls")
        Promote_Project()
    elif ch == 5:
        system("cls")
        Remove_Project()
    elif ch == 6:
        system("cls")
        Search_project()
    elif ch == 7:
        system("cls")
        print("{:>60}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()

def worksTable():
    print("{:>60}".format("-->> WORKS ON TABLE <<--"))    
    print("1. Add WORKS")
    print("2. Display WORKS Record")
    print("3. Update WORKS Record")
    print("4. Remove WORKS Record")
    print("5. Search WORKS Record")
    print("6. Exit\n")
    print("{:>66}".format("-->> Choice Options: [1/2/3/4/5/6] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        add_works()
    elif ch == 2:
        system("cls")
        Display_works()
    elif ch == 3:
        system("cls")
        Update_Works()
    elif ch == 4:
        system("cls")
        Remove_works()
    elif ch == 5:
        system("cls")
        Search_works()
    elif ch == 6:
        system("cls")
        print("{:>60}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()

# Menu function to display menu
def menu():
    system("cls")
    print("{:>80}".format("************************************"))
    print("{:>80}".format("-->> Employee Management System <<--"))
    print("{:>80}".format("************************************"))
    print("1. Employee TABLE")
    print("2. ATTENDANCE TABLE")
    print("3. DEPARTMENT TABLE")
    print("4. DEPENDENT TABLE")
    print("5. JOB_TITLE TABEL")
    print("6. PROJECT TABEL")
    print("7. WORKS TABEL")
    print("8. Exit\n")
    print("{:>85}".format("-->> Choice Options: [1/2/3/4/5/6/7/8] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        employeeTable()
    elif ch == 2:
        system("cls")
        attendanceTable()
    elif ch == 3:
        system("cls")
        departmentTable()
    elif ch == 4:
        system("cls")
        dependentTable()
    elif ch == 5:
        system("cls")
        jobtitleTable()
    elif ch == 6:
        system("cls")
        projectTable()
    elif ch == 7:
        system("cls")
        worksTable()
    elif ch == 8:
        system("cls")
        print("{:>80}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()

menu()
