from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.zj3dr.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# Get the students collection 
students = db.students

# Method to find all students in the collection 
student_list = students.find({})

print("\n Displaying all documents in the collection before any updates using the find() method")

# Get student information from the collection using a loop. 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Calling the update_one method to update last name from 'Henry' to 'Benzema'.
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Benzema"}})

# Using find_one method to find the updated document.
thierry = students.find_one({"student_id": "1007"})

# Output the updated document
print("\n Displaying the updated document for student_id : 1007 using the find_one() method")

print("  Student ID: " + thierry["student_id"] + "\n  First Name: " + thierry["first_name"] + "\n  Last Name: " + thierry["last_name"] + "\n")
 
