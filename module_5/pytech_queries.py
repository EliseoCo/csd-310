from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.zj3dr.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# Get students collection 
students = db.students

# Method to find all students in the collection 
student_list = students.find({})

print("\n Displaying all documents in the collection using the find() method")

# Get student information from the collection using a loop. 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Using find_one method to find only one document.
patrick = students.find_one({"student_id": "1009"})

# Output
print("\n Displaying only one document from the collection using the find_one() method")

print("  Student ID: " + patrick["student_id"] + "\n  First Name: " + patrick["first_name"] + "\n  Last Name: " + patrick["last_name"] + "\n")
 
input("\n\n  End of program, press any key to continue...")
