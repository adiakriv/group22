
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


