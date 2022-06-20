from pymongo import MongoClient

url="mongodb+srv://admin:admin@cluster0.vfvavqz.mongodb.net/pytech?retryWrites=true&w=majority"

# Insert 3 student documents into the PyTech students
client = MongoClient(url) # Connect to MongoDB
db = client.pytech # Connect to the pytech database
students = db.students # Connect to the students students

# use the find method to retrieve all documents
for student in students.find({},{'_id':0}):
    print(student)

print("\n")


# insert a new student document
student_to_insert = {
    "Student ID": "1010",
    "First Name": "Riley",
    "Last Name": "Dorrington",
}

# insert the student document
students.insert_one(student_to_insert)

# find the student with the ID of 1010, get ready to delete it
student_to_delete = students.find_one({"Student ID": "1010"},{'_id':0})

# print the student document before deleting it
print("Student to Be Deleted ==> " + str(student_to_delete))
print("\n")

# delete the student document with the ID of 1010
for student in students.find_one({"Student ID": "1010"}):
    students.delete_one({"Student ID": "1010"})

# use the find method to retrieve all documents after the deletion
for student in students.find({}, {'_id':0}):
    print(student)

print("\n")