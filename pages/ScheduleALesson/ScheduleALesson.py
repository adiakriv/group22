
from flask import render_template, request
from flask import Blueprint

# about blueprint definition
ScheduleALesson = Blueprint(
    'ScheduleALesson',
    __name__,
    static_folder='static',
    static_url_path='/ScheduleALesson',
    template_folder='templates'
)
# Routes
# @ScheduleALesson.route('/schedulealesson')
# def ScheduleALessonFunc():
#     return render_template('ScheduleALesson.html')
#

from flask import flash, redirect, url_for
from MongoDB import check_availability


@ScheduleALesson.route('/schedulealesson', methods=['GET', 'POST'])
def ScheduleALessonFunc():
    if request.method == 'POST':
        # Retrieve the date and time from the form data
        date = request.form.get('date')
        time = request.form.get('time')

        # Call the check_availability function
        available, teacher_id = check_availability(date, time)

        if available:
            # Flash a message
            flash('The lesson has been set successfully')
        else:
            # Flash a message
            flash('The teacher is not available at the selected time and date. Please try again.')

        # Redirect the user to the appropriate page
        return redirect(url_for('HomePageFunc'))

    return render_template('ScheduleALesson.html')

