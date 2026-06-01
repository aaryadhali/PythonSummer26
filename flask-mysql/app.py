import os
from flask import Flask, request, render_template, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)#creates an instance of the flask 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning
db = SQLAlchemy(app)

class employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), unique = False, nullable = False)
    last_name = db.Column(db.String(20), unique = False, nullable = False)
    hire_date = db.Column(db.Date, default = db.func.current_date())
    salary = db.Column(db.Numeric(10,2))

    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"
    
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique = True, nullable = False)

    def __repr__(self):
        return f"User(name = {self.fname} {self.lname}, email = {self.email})"

#login 
@app.route('/', methods = ["GET"])
def login():
    return render_template("index.html")
@app.route('/login_endpoint')
def login_info():
    
#create a user
@app.route('/add_data')
def add_data():
    return render_template('add_profile.html')

@app.route('/create_data')
def create_new_user():
    return render_template('create_user.html')

@app.route('/register', methods = ["POST"])
def registration():
    user_name   = request.form.get("username")
    first_name  = request.form.get("name")
    last_name   = request.form.get("lastname")
    email       = request.form.get("email")
    password    = request.form.get("password") 

    if user_name != '' and first_name != '' and last_name != '' and email != '' and password != '':
        p = UserModel(first_name=first_name, last_name=last_name,password = password, email=email, user_name = user_name)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')
    


@app.route('/add', methods=["POST"])
def profile():
    user_name = request.form.get("user_name")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    password = request.form.get("password")
    email = request.form.get("email")

    if user_name != '' and first_name != '' and last_name != '' and password != '' and email != '':
        p = UserModel(first_name=first_name, last_name=last_name,password = password, email=email, user_name = user_name)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')


if __name__ == "__main__":
    # with app.app_context():  # Needed for DB operations
    #     db.create_all()      # Creates the database and tables
    app.run(debug=True)