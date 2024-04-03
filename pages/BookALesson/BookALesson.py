from flask import render_template
from flask import Blueprint
from flask import request

# about blueprint definition
BookALesson = Blueprint(
    'BookALesson',
    __name__,
    static_folder='static',
    static_url_path='/bookalesson',
    template_folder='templates'
)
# Routes
@BookALesson.route('/bookalesson', methods=['GET', 'POST'])
def BookALessonFunc():
    # subject = request.form['subject']
    # price = request.form['price']
    # location = request.form['location']


    return render_template('BookALesson.html')

