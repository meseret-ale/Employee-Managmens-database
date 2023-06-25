DROP DATABASE IF EXISTS EmployeeDB;
CREATE DATABASE EmployeeDB;
use EmployeeDB;

CREATE TABLE JOB_TITLES (
    JOB_TITLE_ID varchar(255) NOT NULL PRIMARY KEY,
    min_salary BIGINT(20) not NULL,
    max_salary BIGINT(20) not NULL

);

CREATE TABLE EMPLOYEE (
    EMPLOYEE_ID INT NOT NULL PRIMARY KEY,
    birth_date DATE NULL,
    first_name varchar(255) not NULL,
    middle_name varchar(255) NULL,
    last_name varchar(255) NULL,
    sex varchar(255) not NULL,
    salary BIGINT(20) not NULL,
    addres TEXT(255) not NULL,
    Supervisor_ID INT,
    JOB_TITLE_ID varchar(255),
    FOREIGN KEY (JOB_TITLE_ID) REFERENCES JOB_TITLES(JOB_TITLE_ID),
    FOREIGN KEY (Supervisor_ID) REFERENCES EMPLOYEE(EMPLOYEE_ID)

);

CREATE TABLE dependent (
    dependent_name varchar(255) NOT NULL PRIMARY KEY,
    birth_date DATE not NULL,
    relationship varchar(255) NULL,
    sex varchar(255) not NULL,
    EMPLOYEE_ID INT,
    FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEE(EMPLOYEE_ID)

);

CREATE TABLE department (
    department_name varchar(255) NOT NULL PRIMARY KEY,
    number_of_employee int(11) not NULL,
    location varchar(234) not NULL,
    start_date DATE not NULL,
    EMPLOYEE_ID INT,
    FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEE(EMPLOYEE_ID)

);

CREATE TABLE project (
    project_name varchar(255) NOT NULL PRIMARY KEY,
    budget BIGINT(20) not NULL,
    location varchar(234) not NULL,
    department_name varchar(255),
    FOREIGN KEY (department_name) REFERENCES department(department_name)

);

CREATE TABLE works (
    EMPLOYEE_ID INT NOT NULL,
    project_name varchar(255) NOT NULL,
    CONSTRAINT pk_works PRIMARY KEY (EMPLOYEE_ID, project_name),
    hours INT(11) not NULL,
    start_date DATE not NULL,
    FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEE(EMPLOYEE_ID),
    FOREIGN KEY (project_name) REFERENCES project(project_name)
    
);

CREATE TABLE attendance (
    attendance_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    attendance_date DATE not NULL,
    check_in_time TIME not NULL,
    check_out_time TIME not NULL,
    EMPLOYEE_ID INT NOT NULL,
    FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEE(EMPLOYEE_ID)

);
