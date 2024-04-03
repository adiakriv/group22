from flask import render_template
from flask import Blueprint

# about blueprint definition
CreateAnAccount = Blueprint(
    'CreateAnAccount',
    __name__,
    static_folder='static',
    static_url_path='/CreateAnAccount',
    template_folder='templates'
)
# Routes
@CreateAnAccount.route('/createanaccount')
def reateAnAccountFunc():
    return render_template('CreateAnAccount.html')