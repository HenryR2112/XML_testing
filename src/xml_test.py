import xml.etree.ElementTree as ET
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('test_database.db')

# Create a cursor object to interact with the database
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS test (
    name TEXT,
    id TEXT,
    department TEXT
)
''')

# Reading the XML file, file name is test.xml
tree = ET.parse('xml_files/test.xml')

# In our XML file, 'student' is the root for all student data.
data2 = tree.findall('student')

# Retrieving the data and inserting it into the table
# 'j' value for printing number of values that are stored
for i, j in zip(data2, range(1, 6)):
    name = i.find('name').text
    id = i.find('id').text
    department = i.find('department').text

    # SQL query to insert data into database
    data = """INSERT INTO test (name, id, department) VALUES (?, ?, ?)"""

    # Executing cursor object
    c.execute(data, (name, id, department))
    conn.commit()
    print("test student No-", j, " stored successfully")

# Close the connection
conn.close()
