from flask import Flask, request, render_template ,jsonify
import json

app = Flask(__name__)

class Employee:
    data = ["a","b"]
    id
    def __init__(self, pid):
        self.id = pid
        if pid in self.data:
            print("this employee already exists")
            return  # stop here!
        elif len(self.data) < pid:
            # for i in range(pid-len(self.data)):
            while len(self.data) <= pid:
                self.data.append("")
            self.data[pid]=pid
        else:
            self.data.insert(pid, pid)
    
    def get_id(self):
        print(self.data)
        return self.data[self.id]

    # def del_employee(self, pid):
    #     if pid in self.data:
    #         del self.data[]


e1 = Employee(1)
print(e1.get_id())
print(len(e1.data))
e2 = Employee(10)
print(e2.get_id())
e3 = Employee(30)
print(e3.get_id())
e4 = Employee(20)
print(e4.get_id())
e5 = Employee(11)
print(e5.get_id())
e6 = Employee(11)
print(e6.get_id())
print(e1.get_id())



employeesn = [e1,e2,e3,e4,e5]
import jsonpickle

@app.route('/employee',methods = ["GET"])
def getAllEmployees():
    json_string = json.dumps([ob.__dict__ for ob in employeesn])
    return(json_string)

    # json_data = json.dumps(employeesn, 
    #                        default=lambda o: o.__dict__, 
    #                        indent=4)
    # return json_data

@app.route('/employee',methods = ["POST"])
def createEmployee():
    data = request.get_json() #gets json as a dictionary
    pid = data.get('pid') #.get targets the key (pid) and returns the value
    pid = int(pid) #just incase the dictionary data is not returned as an int
    e = Employee(pid)
    employeesn.append(e)
    print(employeesn)
    e.get_id()
    return f"hello {pid}, POST request received"
    #return render_template('name.html')
    #e = Employee(pid)
    #return e

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