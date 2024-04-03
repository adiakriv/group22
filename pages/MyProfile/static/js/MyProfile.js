document.addEventListener("DOMContentLoaded", function() {
    const cancelButtonList = document.querySelectorAll('.cancel-button');
    const updateButton = document.querySelector('.submit-button');
    const uploadForm = document.querySelector('form[action="/upload"]');
    const fileInput = document.getElementById('fileInput');
    const lessonsList = document.querySelector('.lessons-list');
    const profileForm = document.querySelector('.form_container');
    const updateProfileLink = document.querySelector('.submit-button');

    // Function to handle lesson cancellation confirmation
    function confirmLessonCancellation(lessonItem) {
        const confirmation = confirm("Are you sure you want to cancel the lesson?");
        if (confirmation) {
            lessonItem.parentNode.removeChild(lessonItem);
            alert("The lesson has been successfully canceled.");

        }
    }

    // Event listener for lesson cancellation
    cancelButtonList.forEach(function(cancelButton) {
        cancelButton.addEventListener('click', function(event) {
            event.preventDefault();
            const lessonItem = this.parentNode;
            confirmLessonCancellation(lessonItem);
        });
    });

    // Event listener for profile update
    updateButton.addEventListener('click', function(event) {
        event.preventDefault();

        // Validate profile before updating
        if (validateProfile()) {
            // Perform profile update logic here
            alert("Profile has been successfully updated.");
        }
    });

    // Function to validate profile inputs
    function validateProfile() {
        const firstName = document.querySelector('input[name="FirstName"]').value.trim();
        const lastName = document.querySelector('input[name="LastName"]').value.trim();
        const email = document.querySelector('input[name="Email"]').value.trim();
        const phone = document.querySelector('input[name="phoneNumber"]').value.trim();
        const age = parseInt(document.querySelector('input[name="Age"]').value.trim(), 10);

        if (firstName.length > 50 || lastName.length > 50) {
            alert("First name and last name cannot exceed 50 characters.");
            return false;
        }

        if (!validateEmail(email)) {
            alert("Please enter a valid email address.");
            return false;
        }

        if (!validatePhoneNumber(phone)) {
            alert("Please enter a valid 10-digit phone number.");
            return false;
        }

        if (!validateAge(age)) {
            alert("Please enter a valid age between 5 and 100.");
            return false;
        }

        return true;
    }

    // Function to validate email format
    function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    // Function to validate phone number
    function validatePhoneNumber(phoneNumber) {
        const regex = /^\d{10}$/;
        return regex.test(phoneNumber);
    }

    // Function to validate age
    function validateAge(age) {
        return age >= 5 && age <= 100;
    }

    uploadForm.addEventListener('submit', function(event) {
        event.preventDefault();

        if (fileInput.files.length > 0) {
            alert("Image has been successfully uploaded.");
        } else {
            alert("Please select an image.");
        }
    });
    updateProfileLink.addEventListener('click', function(event) {
        event.preventDefault();


    });
});
const formContainer = document.querySelector('.form-container');


const cancelButton = document.createElement('button');
cancelButton.classList.add('cancel-button');
cancelButton.textContent = 'Cancel';

newLessonItem.appendChild(cancelButton);


const lessonsList = formContainer.querySelector('.lessons-list');

lessonsList.appendChild(newLessonItem);


const cancelButtons = document.querySelectorAll('.cancel-button');
cancelButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove the parent li element when the cancel button is clicked
        button.parentNode.remove();
    });
});

// Add event listener to the "Update my profile" link
const updateProfileLink = document.querySelector('.submit-button');
updateProfileLink.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent the default action of the link
    // Add your code here to handle updating the profile
    console.log('Updating profile...');
    // You can send a request to update the profile here
});
