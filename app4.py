from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

if __name__ == "__main__":
    app.run()