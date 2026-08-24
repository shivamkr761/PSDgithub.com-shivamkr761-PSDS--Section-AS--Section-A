CREATE DATABASE college_db;

USE college_db;

CREATE TABLE Department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,

    FOREIGN KEY (department_id)
        REFERENCES Department(department_id)
);
show Tables;