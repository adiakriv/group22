from flask import render_template, request, session, redirect, url_for
from flask import Blueprint

BookALesson = Blueprint(
    'BookALesson',
    __name__,
    static_folder='static',
    static_url_path='/bookalesson',
    template_folder='templates'
)

@BookALesson.route('/bookalesson', methods=['GET', 'POST'])
def BookALessonFunc():
    if request.method == 'POST':
        return redirect(url_for('TeacherProfile.TeacherProfileFunc'))  # Redirect to the 'Teacher Profile' page
    return render_template('BookALesson.html')

