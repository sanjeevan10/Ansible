import os
from flask import Flask
import mysql.connector

app = Flask(__name__)

mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or  'localhost'

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="db_user",
    password="Passw0rd",
    database="employee_db"
)
cursor = db.cursor()

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/read from database')
def read():
    cursor.execute("SELECT * FROM employees")
    row = cursor.fetchone()
    result = []
    while row is not None:
      result.append(row[0])
      row = cursor.fetchone()

    return ",".join(result)

if __name__ == '__main__':
    app.run(debug=True)
