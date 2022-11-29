#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('school.db')
print("Opened Database")

conn.execute(''' CREATE TABLE IF NOT EXISTS STUDENTS
        (STUDENTID  INT    PRIMARY KEY   NOT NULL,
         NAME       TEXT                 NOT NULL,
         AGE        INT                  NOT NULL,
         GPA        REAL                 NOT NULL);''')


students= [
        {"StudentID": 1, "name": "Paul", "age": 8, "gpa": 3.2},
        {"StudentID": 2, "name": "Allen", "age": 9, "gpa": 4.0},
        {"StudentID": 3, "name": "Time", "age": 10, "gpa": 2.2},
        ]

for student in students:
    studentid = student['StudentID']
    name = student['name']
    age = student['age']
    gpa = student['gpa']


    conn.execute(f"INSERT INTO STUDENTS (STUDENTID, NAME, AGE, GPA) VALUES ({studentid},'{name}', {age}, {gpa})")
    conn.commit()

conn.close()    
