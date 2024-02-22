document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();

        var firstName = document.querySelector('input[name="FirstName"]').value;
        var lastName = document.querySelector('input[name="LastName"]').value;
        var email = document.querySelector('input[name="Email"]').value;
        var password = document.querySelector('input[name="password"]').value;
        var phoneNumber = document.querySelector('input[name="phoneNumber"]').value;
        var age = document.querySelector('input[name="Age"]').value;

        if (firstName.length > 30) {
            alert('First name must be less than 30 characters.');
            return;
        }

        if (lastName.length > 50) {
            alert('Last name must be less than 50 characters.');
            return;
        }

        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Invalid email format.');
            return;
        }

        if (password.length < 8 || !/\d/.test(password) || !/[a-zA-Z]/.test(password)) {
            alert('Password must be at least 8 characters long and contain both letters and numbers.');
            return;
        }

        var phoneRegex = /^0\d{9}$/;
        if (!phoneRegex.test(phoneNumber)) {
            if (!phoneNumber.startsWith('0')) {
                alert('Phone number must start with 0.');
            } else if (phoneNumber.length !== 10) {
                alert('Phone number must be exactly 10 digits long.');
            } else {
                alert('Invalid phone number format. Please enter 10 digits starting with 0 without spaces or special characters.');
            }
            return;
        }

        if (age < 5 || age > 100) {
            alert('Age must be between 5 and 100.');
            return;
        }

        this.submit();
    });

    // Additional check for empty fields
    var submitButton = document.querySelector(".submit-button");
    submitButton.addEventListener("click", function(event) {
        var inputs = document.querySelectorAll("input");
        var allFieldsFilled = true;

        inputs.forEach(function(input) {
            if (input.value === "") {
                allFieldsFilled = false;
            }
        });

        if (!allFieldsFilled) {
            alert("Please fill in all the fields.");
            event.preventDefault();
        }
    });
});
