from flask import Flask
import sqlite3

app = Flask(__name__)

class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect(':memory:')
        return cls._instance

@app.route('/')
def home():
    db1 = DatabaseSingleton() # DB instance for user 1
    db2 = DatabaseSingleton() # DB instance for user 2
    return f"Is the same instance: {db1 is db2}"

if __name__ == "__main__":
    app.run(debug=True)