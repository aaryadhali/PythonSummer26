from flask import Flask
from sqlalchemy import SQLAlchemy

app = Flask(__name__) #creates your app instance. __name__ tells Flask where to find templates/static files.