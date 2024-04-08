from flask import render_template, session, redirect, request, flash
from MongoDB import users
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
@TeacherForYou.route('/', methods=['GET', 'POST'])
def TeacherForYouFunc():
    if request.method == 'POST':
        email = request.form.get('email')
        from MongoDB import users
        user = users.find_one({'email': email})
        if user:
            session['email'] = email
            return redirect('/homepage')
        else:
            flash('User does not exist')
            return render_template('TeacherForYou.html')
    else:
        if session.get('email') is None or session.get('email') == '':
            return render_template('TeacherForYou.html')
        else:
            return redirect('/homepage')