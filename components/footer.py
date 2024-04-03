from flask import Blueprint, render_template
from flask import session, redirect

# navbar blueprint definition
navbar = Blueprint('footer', __name__, static_folder='static', static_url_path='/footer', template_folder='templates')

