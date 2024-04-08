from flask import Flask
from MongoDB import *

app = Flask(__name__)
app.config.from_pyfile('settings.py')

#ContactUs
from pages.ContactUs.ContactUs import ContactUs
app.register_blueprint(ContactUs)

#Homepage
from pages.HomePage.HomePage import HomePage
app.register_blueprint(HomePage)

## TeacherForYou
from pages.TeacherForYou.TeacherForYou import TeacherForYou
app.register_blueprint(TeacherForYou)

## TeacherProfile
from pages.TeacherProfile.TeacherProfile import TeacherProfile
app.register_blueprint(TeacherProfile)

## ScheduleALesson
from pages.ScheduleALesson.ScheduleALesson import ScheduleALesson
app.register_blueprint(ScheduleALesson)

## MyProfile
from pages.MyProfile.MyProfile import MyProfile
app.register_blueprint(MyProfile)

## CreateAnAccount
from pages.CreateAnAccount.CreateAnAccount import CreateAnAccount
app.register_blueprint(CreateAnAccount)

###### BookALesson
from pages.BookALesson.BookALesson import BookALesson
app.register_blueprint(BookALesson)

#app.register_blueprint(BookALesson)



