
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from settings import MONGO_URI
from app import *


uri = MONGO_URI
client = MongoClient(uri, server_api=ServerApi('1'))
Db = client['TeacherForYou']
users = Db['Users']
teachers = Db['Teachers']
lessons = Db['Lessons']

def find_teachers(subject, city):
    teachers = Db['Teachers']
    # Query the collection
    results = teachers.find({
        "subject": subject,
        "city": city
    })
    # Convert the results to a list
    teachers_list = list(results)
    return teachers_list

def check_availability(date, time):
    # Combine date and time into a single string
    date_time = f"{date}T{time}"

    # Find all teacher documents
    all_teachers = teachers.find()

    # Iterate over each teacher document
    for teacher in all_teachers:
        # Check if the date_time is in the available array of the teacher document
        if date_time in teacher['available']:
            return True, str(teacher['_id'])

    # If the date_time is not found in any available array, return False
    return False, None