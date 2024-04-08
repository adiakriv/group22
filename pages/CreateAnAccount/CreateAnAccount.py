from flask import render_template, redirect, session
from flask import Blueprint, request

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
def CreateAnAccountFunc():
    return render_template('CreateAnAccount.html')


@CreateAnAccount.route('/createanaccount', methods=['GET', 'POST'])
def createanacount():
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        email = request.form['Email']
        password = request.form['password']
        phone = request.form['phoneNumber']
        age = request.form['Age']
        print(userExist(email))
        if(userExist(email)):
            ##put user in DB
            #todo: add error message
            return "try againnnnn"
        else:
            putUserInDB(FirstName, LastName, email, password, phone, age)
            session['email'] = email
            return redirect('/homepage')
    else:
        return render_template('CreateAnAccount.html')



def userExist(email):
    from MongoDB import users
    if users.find_one({'email': email}):
        return True
    else:
        return False

def putUserInDB(FirstName, LastName, email, password, phone, age):
    from MongoDB import users
    users.insert_one({'firstName': FirstName, 'lastName': LastName, 'email': email, 'password': password, 'phone': phone, 'age': age})
    return True @CreateAnAccount.route('/createanacount', methods=['GET', 'POST'])
def createanacount():
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        email = request.form['Email']
        password = request.form['password']
        phone = request.form['phoneNumber']
        age = request.form['Age']
        print(userExist(email))
        if(userExist(email)):
            ##put user in DB
            #todo: add error message
            return "try againnnnn"
        else:
            putUserInDB(FirstName, LastName, email, password, phone, age)
            session['email'] = email
            return redirect('/homepage')
    else:
        return render_template('CreateAnAccount.html')