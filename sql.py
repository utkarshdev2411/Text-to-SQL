import sqlite3

#connect sqlite3
connection = sqlite3.connect('student.db')

#Cursor object to execute SQL commands such as CREATE, INSERT, SELECT, UPDATE, DELETE

cursor=connection.cursor()

##Create table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR (25), SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

##Insert data
cursor.execute('''INSERT INTO STUDENT VALUES('Rahul','Information Technology','A',40)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Rohit','Data Science','B',80)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Raj','Information Technology','C',70)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Ramit','Data Science','A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Keshav','Data Science','A',90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Aman','Information Technology','C',74)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Aryan','Data Science','B',56)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Anurag','Information Technology','A',67)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Vinita','Data Science','C',78)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Raghav','Information Technology','A',89)''')


##Display data
print("The inserted records are:")
data=cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

 ##CLose the connection
connection.commit()
connection.close()   