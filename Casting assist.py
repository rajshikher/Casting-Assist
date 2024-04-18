import sqlite3

# Connect to SQLite database (replace 'chatbot.db' with your database file name).
conn = sqlite3.connect('./chatbot.db')

# Create a cursor object to execute SQL queries.
cursor = conn.cursor()

# Example: Execute a simple query to fetch data.
cursor.execute("SELECT * FROM auditions")
rows = cursor.fetchall()

# Display the fetched data.
for row in rows:
    print(row)
    print("Hello")

# Don't forget to close the connection when done.
conn.close()
