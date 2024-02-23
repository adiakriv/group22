# group22
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

