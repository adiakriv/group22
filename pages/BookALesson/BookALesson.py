from flask import render_template, request, session, redirect, url_for
from flask import Blueprint
from MongoDB import find_teachers

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
        # Extract form data
        subject = request.form.get('subject')
        city = request.form.get('city')

        # Save form data (you can replace this with your own logic)
        session['subject'] = subject
        session['city'] = city

        # Find teachers based on the form data
        teachers = find_teachers(subject, city)
        session['teachers'] = teachers
        # return redirect(url_for('TeacherProfile.TeacherProfileFunc'))  # Redirect to the 'Teacher Profile' page
        return redirect(url_for('TeacherProfile.TeacherProfileFunc', teachers=teachers))
    return render_template('BookALesson.html')