import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="1208",
    database="my_flask_db"
)

c = db.cursor()
employeetbl_select = """SELECT * FROM employees"""
c.execute(employeetbl_select)
employee_data = c.fetchall()

for e in employee_data:
    print(e)
    # e = NewEmployee(e.id , e.firstName)
print()
query = """SELECT employee_id, first_name from employees"""
c.execute(query)
employeedata2 = c.fetchall()
for e in employeedata2:
    print(e)
# insert statement for tblemployee
# this statement will enable us to insert multiple rows at once.
# employeetbl_insert = """INSERT INTO employees (
#    employee_id,
#    first_name,
#    last_name,
#    salary) 
#    VALUES  (%s, %s, %s, %s)"""

# data = [("3","Vani", "HR", "100000"),
#         ("4","Krish", "Accounts", "60000"),
#         ("5","Aishwarya", "Sales", "25000"),
#         ("6","Govind", "Marketing", "40000")]

# c.executemany(employeetbl_insert, data)
# db.commit()
# finally closing the database connection
db.close()

