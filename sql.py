import sqlite3

## Connect to sqlite
connection=sqlite3.connect("student.db")

##Cursor object to insert record, create table, retrieve
cursor=connection.cursor()

#create the table
table_info="""
Create table Student(NAME VARCHA(25), CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

#insert some records

cursor.execute("""Insert Into STUDENT values('Nishant', 'AIML', 'A', '99')""")
cursor.execute("""Insert Into STUDENT values('Don', 'CSE', 'A', '69')""")
cursor.execute("""Insert Into STUDENT values('Jon', 'DS', 'A', '49')""")
cursor.execute("""Insert Into STUDENT values('Rohan', 'EM', 'A', '59')""")

#display all the records:
print("The inserted records are")

data=cursor.execute("""SELECT * From STUDENT""")

for row in data:
    print(row)

#close the connection
connection.commit()
connection.close()