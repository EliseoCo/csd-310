from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.zj3dr.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# Get the students collection. 
students = db.students

# Calling find method and displaying results to terminal window. 
student_list = students.find({})

print("\n Displaying all documents in the collection before any updates using the find() method: \n")

# Get student information from the collection using a loop. 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# New document with student_id: 1010.
new_doc = {
    "student_id": "1010",
    "first_name": "Michel",
    "last_name": "Platini"
}

# Calling the insert_one method to insert the new document to the collection.
new_doc_inserted = students.insert_one(new_doc).inserted_id

# Calling the find_one() method to find the newly added document.
new_doc = students.find_one({"student_id": "1010"})

# Output the updated document.
print("\n Displaying the new document for student_id 1010 using the find_one() method: \n")
print("  Student ID: " + new_doc["student_id"] + "\n  First Name: " + new_doc["first_name"] + "\n  Last Name: " + new_doc["last_name"] + "\n")
 
# Calling the delete_one() method to delete document with student_id 1010.
new_doc_deleted = students.delete_one({"student_id": "1010"})

# Call the find() method again to display the new results.
new_student_list = students.find({})

print("\n Displaying updated collection after use of delete_one() method: \n")

# Iterate over the new list and display the new collection after the deleted entry. 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
