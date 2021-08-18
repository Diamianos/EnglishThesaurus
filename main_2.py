# This program extends the Thesaurus program to query from a MySQL database rather than a JSON file

import mysql.connector

# Creating the connection to the database
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

# Creating a cursor object
cursor = con.cursor()

# Prompting for user input
word = input("Enter a word: ")

# Passing a SQL query to the database
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word) # line, multiple definitions

# Storing the results in a variable
results = cursor.fetchall()

# Printing out the results if the list is not empty
if results:
    for result in results:
        print(result[1])
else:
    print("Word not found")
