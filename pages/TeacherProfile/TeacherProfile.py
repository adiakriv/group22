from flask import render_template, session
from flask import Blueprint
from pymongo import MongoClient

# Establish a connection to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']  # replace with your database name
teachers_collection = db['teachers']  # r
# about blueprint definition
TeacherProfile = Blueprint(
    'TeacherProfile',
    __name__,
    static_folder='static',
    static_url_path='/TeacherProfile',
    template_folder='templates'
)

# Routes
@TeacherProfile.route('/teacherprofile', methods=['GET'])
def TeacherProfileFunc():
    # Retrieve the matching teachers from the session
    matching_teachers = session.get('matching_teachers', [])

    # Pass the matching teachers to the template
    return render_template('TeacherProfile.html', teachers=matching_teachers)