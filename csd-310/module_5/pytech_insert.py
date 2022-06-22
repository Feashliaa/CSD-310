from pymongo import MongoClient

url="mongodb+srv://admin:admin@cluster0.vfvavqz.mongodb.net/pytech?retryWrites=true&w=majority"

# Insert 3 student documents into the PyTech students
client = MongoClient(url) # Connect to MongoDB
db = client.pytech # Connect to the pytech database
students = db.students # Connect to the students students

student = {"Student ID": "1007", "First Name": "Thorin", "Last Name": "Oakenshield"} # Create a student document
thorin_student_id = students.insert_one(student).inserted_id # Insert the student document
print(thorin_student_id) # Print the ID of the inserted document

student = {"Student ID": "1008", "First Name": "Bilbo", "Last Name": "Baggins"} # Create a student document
bilbo_student_id = students.insert_one(student).inserted_id # Insert the student document
print(bilbo_student_id) # Print the ID of the inserted document

student = {"Student ID": "1009", "First Name": "Frodo", "Last Name": "Baggins"} # Create a student document
frodo_student_id = students.insert_one(student).inserted_id # Insert the student document
print(frodo_student_id) # Print the ID of the inserted document