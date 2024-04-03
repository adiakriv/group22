
from flask import render_template
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
@ScheduleALesson.route('/schedulealesson')
def ScheduleALessonFunc():
    return render_template('ScheduleALesson.html')


