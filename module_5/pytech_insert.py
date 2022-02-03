from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.zj3dr.mongodb.net/pytech?retryWrites=true&w=majority" 
client = MongoClient(url)
db = client.pytech

# First document
thierry = {
    "student_id": "1007",
    "first_name": "Thierry",
    "last_name": "Henry",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "January 3, 2022",
            "end_date": "March 6, 2022",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Mathew Longley",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Mathew Longley",
                    "grade": "A+"
                }
            ]
        }
    ]

}

# Second document 
zinedine = {
    "student_id": "1008",
    "first_name": "Zinedine",
    "last_name": "Zidane",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "January 3, 2022",
            "end_date": "March 6, 2022",
            "courses": [
                {
                   "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Mathew Longley",
                    "grade": "A+"
                },
                {
                     "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Mathew Longley",
                    "grade": "A+"
                }
            ]
        }
    ]
}

# Third document
patrick = {
    "student_id": "1009",
    "first_name": "Patrick",
    "last_name": "Viera",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "January 3, 2022",
            "end_date": "March 6, 2022",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Mathew Longley",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Mathew Longley",
                    "grade": "A+"
                }
            ]
        }
    ]
}

# Get student collection
students = db.students

# Output
print("\n  -- INSERTING STATEMENTS --")
thierry_student_id = students.insert_one(thierry).inserted_id
print("Student record for Thierry Henry has been added to students collection with document_id " + str(thierry_student_id))

zinedine_student_id = students.insert_one(zinedine).inserted_id
print("Student record for Zinedine Zidane has been added to students collection with document_id " + str(zinedine_student_id))

patrick_student_id = students.insert_one(patrick).inserted_id
print("Student record for Patrick Viera has been added to students collection with document_id " + str(patrick_student_id))

input("\n\n  End of program, press any key to exit... ")
