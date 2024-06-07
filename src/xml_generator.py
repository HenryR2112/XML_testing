import xml.etree.ElementTree as ET
import random
import os

# Define sets of names and occupations
names = ['John', 'Emma', 'Michael', 'Sophia', 'William']
occupations = ['Engineer', 'Doctor', 'Teacher', 'Artist', 'Scientist']

# Create 100 XML files
for i in range(1, 101):
    # Generate random file name
    file_name = f'data_{i}.xml'
    file_path = os.path.join('xml_files', file_name)

    # Create XML structure
    root = ET.Element('studentdata')

    # Generate random student data
    for j in range(5):
        student = ET.SubElement(root, 'student')
        name = random.choice(names)
        id = random.randint(1, 7999)  # Generate random ID
        department = random.choice(occupations)

        # Add student data to XML
        ET.SubElement(student, 'name').text = name
        ET.SubElement(student, 'id').text = str(id)
        ET.SubElement(student, 'department').text = department

        # Randomly decide whether to include GPA
        if random.random() < 0.5:  # 50% chance of including GPA
            gpa = round(random.uniform(2.0, 4.0), 2)  # Generate random GPA
            ET.SubElement(student, 'gpa').text = str(gpa)  # Add GPA to XML

    # Write XML to file
    tree = ET.ElementTree(root)
    tree.write(file_path)

    print(f"Generated XML file: {file_name}")

print("All XML files created successfully.")
