import xml.etree.ElementTree as ET
import sqlite3
import os

# Define the path to the SQLite database file in the root directory
db_path = os.path.join(os.getcwd(), 'test_database.db')

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(db_path)

# Create a cursor object to interact with the database
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS test (
    name TEXT,
    id TEXT PRIMARY KEY,
    department TEXT,
    gpa REAL  -- Add the GPA column
)
''')

# List of XML file paths
xml_files = []  # Add more file paths if needed
for i in range(1, 101):
    # Generate random file name
    file_name = f'data_{i}.xml'
    file_path = os.path.join('xml_files', file_name)
    xml_files.append(file_path)

# Loop through each XML file
for xml_file in xml_files:
    try:
        # Reading the XML file
        tree = ET.parse(xml_file)

        # In our XML file, 'student' is the root for all student data.
        data2 = tree.findall('student')

        # Retrieving the data and inserting it into the table
        for student in data2:
            name = student.find('name').text
            id = student.find('id').text
            department = student.find('department').text

            # Handling GPA
            gpa_element = student.find('gpa')
            gpa = float(gpa_element.text) if gpa_element is not None else None

            # Check if the record already exists in the database
            c.execute("SELECT id FROM test WHERE name=? AND department=? AND gpa=?", (name, department, gpa))
            existing_record = c.fetchone()

            if existing_record:
                print(f"Student '{name}' in department '{department}' with GPA '{gpa}' already exists in the database. Skipping insertion.")
            else:
                # SQL query to insert data into database
                data = """INSERT INTO test (name, id, department, gpa) VALUES (?, ?, ?, ?)"""

                # Executing cursor object
                c.execute(data, (name, id, department, gpa))
                conn.commit()
                print(f"Student '{name}' with ID '{id}' and GPA '{gpa}' stored successfully from file '{xml_file}'")

    except Exception as e:
        print(f"Error occurred while processing file '{xml_file}': {str(e)}")

# Close the connection
conn.close()
