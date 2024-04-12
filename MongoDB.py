
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