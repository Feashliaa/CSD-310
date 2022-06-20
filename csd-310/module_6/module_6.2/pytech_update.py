from pymongo import MongoClient

url="mongodb+srv://admin:admin@cluster0.vfvavqz.mongodb.net/pytech?retryWrites=true&w=majority"

# Insert 3 student documents into the PyTech students
client = MongoClient(url) # Connect to MongoDB
db = client.pytech # Connect to the pytech database
students = db.students # Connect to the students students

# use the find method to retrieve all documents
for student in students.find():
    print(student)

print("\n")

myquery = { "Student ID": "1007" }
newvalues = { "$set": { "Last Name": "Billy" } }

# Update the first student document
students.update_one(myquery, newvalues)

# find the student with the "Student ID" of 1007
print(students.find_one({"Student ID": "1007"}))