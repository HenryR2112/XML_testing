A processing system from artifically creating and dealing with XML files in a non-relational structure and transforming them into a more
intuitive pandas relational structure for machine learning and processing as it relates to potential underlying trends.
Current iterations does the following:
1. xml_generator - creates 100 xml files using student information with a random ID 1-8000 and 1/2 of the group being assignment a gpa
2. xml_test - creates a sqlite3 DB with the information from the xml files parsed into relational format
3. analysis.ipynb - a psuedo notebook which creates a pandas dataframe from the available DB and runs a dummy linear regression on it

following versions:
1.1 - introduce more complex variable structures
1.2 - migrate from SQLite3 to cloud based DB for ease of storage and maintenance
1.3 - modify generation structure to hint at potential exploitable structures in the hope of rediscovering them in analysis.py
