from flask import render_template
from flask import Blueprint

# about blueprint definition
TeacherProfile = Blueprint(
    'TeacherProfile',
    __name__,
    static_folder='static',
    static_url_path='/TeacherProfile',
    template_folder='templates'
)
# Routes
@TeacherProfile.route('/teacherprofile')
def TeacherProfileFunc():

    return render_template('TeacherProfile.html')