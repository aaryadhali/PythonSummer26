from flask import Flask, request, render_template ,jsonify
import json
import mysql.connector

app = Flask(__name__)

db_config = {
    "host":"127.0.0.1",
    "user":"root",
    "password":"1208",
    "database":"my_flask_db"
}


class NewEmployee:
    data = {}

    def __init__(self,pid):
        self.pid = pid
        if self.pid in Employee.data:
            print(f"Employee {self.pid} already exists")
            return
            
        # Store directly by key; no loops, no empty strings needed
        Employee.data[self.pid] = self.pid

    def get_id(self):
        print(Employee.data)
        return self.pid
    

class Employee:
    data = ["a","b"]
    #id
    def __init__(self, pid):
        self.pid = int(pid)
        if self.pid in self.data:
            print("this employee already exists")
            return  # stop here!
        elif len(self.data) <= self.pid:
            # for i in range(pid-len(self.data)):
            while len(self.data) <= self.pid:
                self.data.append("")
            self.data[self.pid]=self.pid
        else:
            self.data[self.pid]=self.pid
    
    def get_id(self):
        print(self.data)
        return self.pid

    # def del_employee(self, pid):
    #     if pid in self.data:
    #         del self.data[]


e1 = Employee(1)
# print(e1.get_id())
# print(len(e1.data))
e2 = Employee(10)
# print(e2.get_id())
e3 = Employee(30)
#print(e3.get_id())
e4 = Employee(20)
# print(e4.get_id())
e5 = Employee(11)
#print(e5.get_id())
e6 = Employee(11)
#print(e6.get_id())
#print(e1.get_id())
employeesn = [e1,e2,e3,e4,e5]

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/v1/employees',methods = ["GET"])
def getAllEmployees():
    json_string = json.dumps([ob.__dict__ for ob in employeesn])
    return(json_string)

    # json_data = json.dumps(employeesn, 
    #                        default=lambda o: o.__dict__, 
    #                        indent=4)
    # return json_data


@app.route('/v1/employees',methods = ["POST"])
def createEmployee():
    data = request.get_json() #gets json as a dictionary
    pid = data.get('pid') #.get targets the key (pid) and returns the value
    pid = int(pid) #just incase the dictionary data is not returned as an int
    
    if any(emp.get_id() == pid for emp in employeesn):
        return f"{pid} already exists", 409
    
    e = Employee(pid)
    employeesn.append(e)
    print(employeesn)
    e.get_id()
    return f"hello {pid}, POST request received", 201
    #return render_template('name.html')
    #e = Employee(pid)
    #return e
@app.route('/id&fname', methods = ["GET"])#<int:id>&<string:fname>
def getidandfname():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """SELECT employee_id, first_name from employees"""
   
    cursor.execute(query)
    employeedata2 = cursor.fetchall()

    cursor.close()
    conn.close()

    return json.dumps(employeedata2, indent=1)

@app.route('/v2/employees', methods = ["GET"])
def get_all_employees():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * from employees")
    employeesdata = cursor.fetchall()

    cursor.close()
    conn.close

    return jsonify(employeesdata)


@app.route('/v2/employees', methods=["POST"])
def createNewEmployee():
    data = request.json

    conn   = get_db_connection() #db variables are fed into this
    cursor = conn.cursor(dictionary=True) #cursor is from the dbconnection so conn

    id     = data.get('id')
    name   = data.get('name')
    dept   = data.get('dept')
    salary = data.get('salary')

    #check if employee exists by id
    
    cursor.execute("SELECT * FROM employees WHERE `employee_id` = %s", (id,))
    existing = cursor.fetchone() #only returns one row
    if existing:
        return jsonify ({"error": f"employee with id {id} already exists"}), 409
    
    #insert after checking
    query = """INSERT INTO employees (

        employee_id,
        first_name,
        dept,
        salary) 
        VALUES  (%s, %s, %s, %s)"""
    
    cursor.execute(query, (id, name, dept, salary))
        
        # Commit the transaction
    conn.commit()
    cursor.close()
    conn.close()
    return  jsonify({"message": f"A new employee {name} was created successfully with id {id}"}), 201
    
@app.route('/v2/employees', methods = ["PUT"])
def raise_or_demotion():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()

    id = data.get('id')
    salary = data.get('salary')

    query ="""UPDATE employees SET salary = %s WHERE employee_id = %s"""
    cursor.execute(query ,(salary, id))
    conn.commit()
    #result = cursor.fetchone()

    # if not result:
    #     return {"error": "Employee not found"}, 404
    
    # print(result)

    cursor.close()
    conn.close()
    return jsonify({"message": "salary successfully updated" })
    



    

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/login', methods = ['GET', 'POST']) #— Handles both GET and POST
def login():
    if request.method == 'POST':
        name = request.form['username']
        return f"hello {name}, POST request received"
    return render_template('name.html')

@app.route('/greet', methods=['POST'])
def greet():
    # Extract the 'name' from the JSON body of the request
    data = request.get_json()
    print(f"incoming request is =>> {data}")
    name = data.get('name', 'Stranger')
    #print(len(data)+1)
    # Return a JSON response with the greeting
    return jsonify({"message": f"Hello {name}"})

@app.route('/farewell', methods=['POST'])
def farewell():

    data = request.get_json()
    name2 = data.get('name', 'Stranger')
    
    return jsonify({"message": f"Goodbye {name2}"})
if __name__ == '__main__':
    app.run(debug=True) #autmatically restarts when changes are added