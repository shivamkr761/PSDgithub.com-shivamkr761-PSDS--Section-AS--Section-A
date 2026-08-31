CREATE DATABASE HospitalDB;

USE HospitalDB;

CREATE TABLE Department (
    Department_ID INT PRIMARY KEY,
    Department_Name VARCHAR(100) NOT NULL,
    Location VARCHAR(100)
);

CREATE TABLE Doctor (
    Doctor_ID INT PRIMARY KEY,
    Doctor_Name VARCHAR(100) NOT NULL,
    Specialization VARCHAR(100),
    Phone VARCHAR(15),
    Department_ID INT,

    FOREIGN KEY (Department_ID)
        REFERENCES Department(Department_ID)
);


CREATE TABLE Patient (
    Patient_ID INT PRIMARY KEY,
    Patient_Name VARCHAR(100) NOT NULL,
    Age INT,
    Gender VARCHAR(10),
    Phone VARCHAR(15),
    Address VARCHAR(200)
);



CREATE TABLE Room (
    Room_ID INT PRIMARY KEY,
    Room_Number VARCHAR(10) NOT NULL,
    Room_Type VARCHAR(50),
    Status VARCHAR(20)
);


CREATE TABLE Appointment (
    Appointment_ID INT PRIMARY KEY,
    Patient_ID INT,
    Doctor_ID INT,
    Appointment_Date DATE,
    Appointment_Time TIME,
    Status VARCHAR(30),

    FOREIGN KEY (Patient_ID)
        REFERENCES Patient(Patient_ID),

    FOREIGN KEY (Doctor_ID)
        REFERENCES Doctor(Doctor_ID)
);


CREATE TABLE Admission (
    Admission_ID INT PRIMARY KEY,
    Patient_ID INT,
    Room_ID INT,
    Admission_Date DATE,
    Discharge_Date DATE,

    FOREIGN KEY (Patient_ID)
        REFERENCES Patient(Patient_ID),

    FOREIGN KEY (Room_ID)
        REFERENCES Room(Room_ID)
);

SHOW TABLES;