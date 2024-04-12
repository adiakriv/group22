### Part 3
### Brief explanation of the idea
Our website provides a platform for scheduling private lessons according to location in Israel and the topic of the lesson. By filtering the relevant and available teachers according to the user's requirements.

### Sequence
1. The user registers or logs in
2. The user chooses the date and profession that is suitable for him
3. The relevant teachers are shown on the next page
4. Choose a teacher
5. There is a check in the array of dates that the teacher is free whether the selected date is available
6. Setting the private class# server-side implementation

## The structure of the project

The project is organized in a structured folder hierarchy. The structure includes separate folders for HTML, CSS, JavaScript and Python files.
The folders in Fruit are arranged by pages and file types.

## Customer routing requests

The application includes functions to handle any request that comes from a customer.
When a user registers or logs in, the system saves his details and enters them into the DB after checking if the user exists or not. If he creates an account, he is transferred to the main page. There is control over users and saving details in the SESSION of a specific user. In addition, there is a connection of the functions that address the DB, the functions that are performed on the client side and are presented to him, and the functions that connect the DB to the client side. It is also possible to check against the list of teachers if it is indeed possible to set a lesson and if it matches the user's input.

## Database connection and queries

The application connects to a MONGO database (having functions in the MONGODB.PY file). The functions perform all validations in the DB according to the user's input.

## Forms application

The forms on the site are designed so that their action feature points to the page/path to the file that will handle the form data (user input). The data from each form is processed according to the purpose of the form, which may involve selecting, adding, updating or deleting information from the database. When a user enters an input, if suitable results are found, they will be shown to him on the relevant pages (for example on the THEACHERPROFILE page). The output is displayed to the user according to the data in the DB and the requirements he selected.

## HTML for templates

The HTML pages of the application were converted to templates as learned in class by blocks. In addition, on the relevant pages (for example TEACHERPROFILE.HTML), functions were written in blocks that are relevant for displaying output on the HTML page (functions that use the DB).

### Screenshots


# group22 Part 2
## Introduction:
Our website offers a comprehensive solution for arranging private lessons, allowing users to search based on specific criteria like location, price, and lesson topic. The website features a curated list of available teachers, enabling students to find instructors that best suit their requirements.
## important details:
 Since there is no database - the connection to the website is made by a specific USER which we defined as an object in JS.
#### Login details:
* Name: Adi
*  Last Name: Akriv
* Password: A12345678
#### First page of the website: TeacherForYou.html
## pages: 
* We've incorporated a recurring footer element with links to contact that appears consistently across all relevant pages.
PAGES:
* Teacher for you:
User log in or a link to create a new account.
After logging in the user is directed to home page.
* Create an account:
Allows the user to register the system for the first time.
After creating the account, the user is directed to home page.
* Home page:
On this page the user can find all his options on the website. There is an options bar that leads to 3 different pages: book a lesson, my profile and contact us.  There is also an option of sign out. In addition, you can find in this page a short summary of our website so you can get to know us better.
* My profile:
This page allows the user to see all the lessons he booked and gives him the option to cancel a lesson if he wants to. 
In addition, the user can edit and update his profile, including the option to upload a picture.
* Book a lesson:
Allows the user to select the subject he is interested in, the price range he would like to pay for the lesson and the location. This page leads the user to the “teacher profile” page according to his choices. 
* Teacher profile:
This page shows the user a list of all the teachers profiles who match his choices. The user will choose the most suitable teacher for him and will submit the “book a lesson” button. This will lead him to the “schedule a lesson” page.
* Schedule a lesson:
This is the last page of the process of booking a lesson. On this page, the user will select the most suitable and available date and time for the lesson he wants to book. The use will get a message that approves his booking and will lead him back to home page.

## CSS:
We created a customized CSS page for each page. The designs are uniform throughout the pages.

* Responsive Design: Each page is optimized for both mobile viewing and resizing, guaranteeing a seamless experience on various screen sizes.
* Animation: All page titles and visual components, including images, feature dynamic animations, enhancing the visual appeal of the homepage.

## Dynamic realization of the website in javascript:
#### Utilization of JavaScript Files Across All Pages:
* System Login Page (TeacherForYou): Implemented validation ensuring all fields are filled and verified the existence of the user in the system.
* Create Account Page:
Enforced completion of all fields during user creation, with each field undergoing separate validation:
Email validation ensures correct email format.
Password requires letters and numbers, with a minimum length of 8 characters.
Phone number must have 10 digits, starting with 0, and age must be realistic for private lessons.
* Homepage:
Implemented a logout feature, returning the user to the initial window upon clicking "Log Out".
* Contact Us Page:
Enforced completion of all fields when submitting a contact form, displaying an appropriate message if any fields are incomplete.
* My Profile Page:
Provided an option to edit existing profiles.
Implemented a feature to cancel existing classes, displaying an alert message.
Allowed file uploads, restricting file types to images only.
* Teacher Profile Page:Displayed all teachers meeting the student's initial requirements.
Provided a link to schedule a class with the selected teacher.
* Schedule Lesson Page:
Limited class hours to designated times.
Implemented date selection limited to future dates, up to 3 months ahead.
Enforced completion of date fields, displaying relevant messages when setting the class.

## Implementation of Service Functionality on the Client Side:
Validation rules and checks for valid user input are thoroughly examined and enforced within the JavaScript files. In the event of invalid input, users are unable to proceed, and a corresponding warning message is promptly displayed.
When customers are prompted to fill in details in the forms, the information they provide is collected for processing. On the server side, the client's input undergoes validation against the database (which will be connected subsequently). Based on the collected data and the information stored in the database, appropriate messages will be returned to the customer (e.g., successful rate determination, etc.).

#### Additional functionalities that will be implemented in the upcoming phase, including database integration:
* My lessons: Users will be able to view and manage their class schedules, with updates reflected based on the connected database.
* Login Details: User authentication and login credentials will be synchronized with the database, enabling secure access to accounts.
* Photo Upload: Users will have the capability to upload and manage profile photos, with changes reflected in accordance with the connected database.
#### Using the EVENT FUNCTION : There is enforcement when the user clicks on the continue button and all the relevant fields have been filled. Setting a rate - enforcement on a legal date and in the future.

