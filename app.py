import os
from flask import Flask, render_template, request, redirect, url_for
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

# Create a table if not exists
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

@app.route('/')
def index():
    # Fetch all users from the database
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    # Get user name from the form
    name = request.form['name']

    # Insert user into the database
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    db.commit()

    # Redirect to the home page
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
