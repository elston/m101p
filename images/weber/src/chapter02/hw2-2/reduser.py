#!/usr/bin/env python
import pymongo

#..
uri = "mongodb://adminmaster:passmaster@storage/admin"
connection = pymongo.MongoClient(uri)



def remove_doc(doc_id):

    # get a handle to the school database
    db = connection.students
    grades = db.grades
    # ...
    try:
        result = grades.delete_one({'_id':doc_id})
        print("  ==> removed: ", doc_id, result)
    except Exception as e:
        print("Exception: ", type(e), e)

# ..
def find_student_data(student_id):
    # ...
    db = connection.students
    grades = db.grades
    # get a handle to the school database
    print("Searching for student data for student with id = ", student_id)
    try: 
        docs = grades.find({'student_id':student_id,'type': 'homework'})
        doc = min(docs,key=lambda x:x['score'])
        remove_doc(doc['_id'])
    except Exception as e:
        print("Exception: ", type(e), e)

# def find():

#     print("find(), reporting for duty")

#     query = {'type': 'homework'}

#     try:
#         cursor = grades.find(query)

#     except Exception as e:
#         print("Unexpected error:", type(e), e)

#     sanity = 0
#     for doc in cursor:
#         print(doc)
#         sanity += 1
#         if (sanity > 10):
#             break

def find():
    # ..
    db = connection.students
    grades = db.grades
    # ..
    try:
        student_ids = grades.distinct('student_id')
    except Exception as e:
        print("Unexpected error:", type(e), e)
    # ..
    for student_id in student_ids:
        find_student_data(student_id)

if __name__ == '__main__':
    find()
