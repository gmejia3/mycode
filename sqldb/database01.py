#!/usr/bin/python3

import sqlite3 #Part of the python standard library

#Function connect which will connect to a file that will hold all the files/
#.connect will create this file if it doesnt exist.
conn = sqlite3.connect('test.db')

conn.execute("""CREATE TABLE IF NOT EXISTS COMPANY
                (ID       INT       PRIMARY KEY  NOT NULL,
                NAME      TEXT                   NOT NULL,
                AGE       INT                    NOT NULL,
                ADDRESS   CHAR(50),
                SALARY    REAL);
                """)


#           HTTP   SQL
#Create     POST   INSERT
#Read       GET
#Update     PUT
#Delete     DELETE

conn.execute("UPDATE COMPANY set NAME = 'Leo' where ID = 2")
conn.execute("UPDATE COMPANY set NAME = 'Lemon' where ID = 3")
conn.execute("UPDATE COMPANY set NAME = 'Mark' where ID = 5")


#conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (2, 'paul', 32, 'California', 20000.00)")

#conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (3, 'paul', 32, 'California', 20000.00)")
#conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (4, 'paul', 32, 'California', 20000.00)")
print("Opened database successfully")
conn.execute("DELETE from COMPANY where ID = 4")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for x in cursor:
    print("ID = ", x[0])
    print("NAME = ", x[1])
    print("ADDRESS = ", x[2])
    print("SALARY = ", x[3], "\n")
conn.commit()
conn.close()
#Connection closed when script ended

