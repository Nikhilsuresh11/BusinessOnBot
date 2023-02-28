import csv
import sqlite3

# Open a connection to the SQLite database
conn = sqlite3.connect('bank_details.db')
cursor = conn.cursor()

# Create a table to hold the bank details
cursor.execute('''
    CREATE TABLE IF NOT EXISTS banks (
        ifsc TEXT PRIMARY KEY,
        bank_id INTEGER,
        branch TEXT,
        address TEXT,
        city TEXT,
        district TEXT,
        state TEXT,
        bank_name TEXT
    )
''')

# Read the data from the CSV file and insert it into the database
with open('bank_branches.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        cursor.execute('''
            INSERT INTO banks (ifsc, bank_id, branch, address, city, district, state, bank_name)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', row)

# Commit the changes and close the database connection
conn.commit()
conn.close()
