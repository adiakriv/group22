from flask import render_template, session
from flask import Blueprint
from pymongo import MongoClient

TeacherProfile = Blueprint(
    'TeacherProfile',
    __name__,
    static_folder='static',
    static_url_path='/teacherprofile',
    template_folder='templates'
)

@TeacherProfile.route('/teacherprofile', methods=['GET'])
def TeacherProfileFunc():
    # Retrieve the form data from the session

    # Render the template with the teacher's name
    return render_template('TeacherProfile.html')