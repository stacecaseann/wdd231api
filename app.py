from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def fetch_users():
    conn = sqlite3.connect("database.db")  # Connect to SQLite
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")  # Assuming a 'users' table
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1]} for row in rows]  # Convert to JSON

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(fetch_users())  # API returns JSON

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask web server
