#!/usr/bin/env python
import pymongo

#..
uri = "mongodb://adminmaster:passmaster@storage/admin"
connection = pymongo.MongoClient(uri)



def remove_doc(doc_id):

    # get a handle to the school database
    db = connection.school
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
    db = connection.school
    grades = db.grades
    # get a handle to the school database
    print("Searching for student data for student with id = ", student_id)
    try: 
        docs = grades.find({'student_id':student_id,'type': 'homework'})
        doc = min(docs,key=lambda x:x['score'])
        # remove_doc(doc['_id'])
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
    db = connection.school
    students = db.students
    # ..
    try:
        # students = students.find().limit(10)
        students = students.find()
    except Exception as e:
        print("Unexpected error:", type(e), e)
    # ..
    for student in students:
        hw_scores = list(filter(lambda x:x[1]['type']=='homework',enumerate(student['scores'])))
        if len(hw_scores) < 2:
            continue
        # ...
        id_score, score = min(hw_scores,key=lambda x:x[1]['score'])    
        print(student['name'],id_score, score['score'])
        del student['scores'][id_score]
        # ...
        result = db.students.update_one({'_id': student['_id']},
                          {'$set': {'scores': student['scores']}})        



if __name__ == '__main__':
    find()
