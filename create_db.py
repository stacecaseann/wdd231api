import sqlite3

# Connect to SQLite database (creates 'database.db' if it doesn't exist)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create a 'users' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

# Insert sample data
cursor.executemany("INSERT INTO users (name) VALUES (?)", [
    ("Alice",),
    ("Bob",),
    ("Charlie",)
])

# Commit and close
conn.commit()
conn.close()

print("Database 'database.db' created successfully!")
