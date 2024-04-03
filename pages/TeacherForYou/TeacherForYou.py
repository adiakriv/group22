from flask import render_template
from flask import Blueprint

# about blueprint definition
TeacherForYou = Blueprint(
    'TeacherForYou',
    __name__,
    static_folder='static',
    static_url_path='/TeacherForYou',
    template_folder='templates'
)

# Routes
@TeacherForYou.route('/')
def TeacherForYouFunc():
    return render_template('TeacherForYou.html')