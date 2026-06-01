from app import app, db
import mysql.connector

# my = mysql.connector.connect(
#     host
# )

with app.app_context():
    db.create_all()
