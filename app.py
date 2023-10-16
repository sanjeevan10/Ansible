import os
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or  'localhost'

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'db_user',
    'password': 'Passw0rd',
    'database': 'employee_db'  
}

@app.route('/')
def home():
    return render_template('index.html')  

@app.route("/submit", methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']

    connection = mysql.connector.connect(db_config)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), email VARCHAR(255))")
    


    cursor.execute("INSERT INTO users(username,email) VALUES(%S,%S)", (username,email))
    connection.commit()

    connection.close()
    return "success"
    


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
