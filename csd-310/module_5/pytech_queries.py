from pymongo import MongoClient

url="mongodb+srv://admin:admin@cluster0.vfvavqz.mongodb.net/pytech?retryWrites=true&w=majority"

# Insert 3 student documents into the PyTech students
client = MongoClient(url) # Connect to MongoDB
db = client.pytech # Connect to the pytech database
students = db.students # Connect to the students students

# Testing the find method
for student in students.find(): # Prints all the students in the database
    print(student)

print("\n") # Print a blank line

# Print the student with the student id of 1007 - Testing the find_one() method
print(students.find_one({"Student ID": "1007"}))