from flask import render_template, session, redirect, url_for
from flask import Blueprint

# about blueprint definition
HomePage = Blueprint(
    'HomePage',
    __name__,
    static_folder='static',
    static_url_path='/HomePage',
    template_folder='templates'
)
# Routes
@HomePage.route('/homepage')
@HomePage.route('/home')
def HomePageFunc():
    return render_template('HomePage.html')
@HomePage.route('/logout')
def logout():
    # Clear the user's session
    session.clear()
    # Redirect the user to the login page
    return redirect(url_for('TeacherForYou.TeacherForYouFunc'))