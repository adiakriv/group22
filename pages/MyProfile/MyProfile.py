from flask import render_template
from flask import Blueprint

# about blueprint definition
MyProfile = Blueprint(
    'MyProfile',
    __name__,
    static_folder='static',
    static_url_path='/MyProfile',
    template_folder='templates'
)
# Routes
@MyProfile.route('/myprofile')
def MyProfileFunc():
    return render_template('MyProfile.html')

