function handleFormSubmission(event) {
    event.preventDefault();

    var firstName = document.querySelector('input[name="FirstName"]').value;
    var lastName = document.querySelector('input[name="LastName"]').value;
    var password = document.querySelector('input[name="password"]').value;

    if (firstName.trim() === '' || lastName.trim() === '' || password.trim() === '') {
        alert('Please fill in all fields.');
        return;
    }

    // Check if the entered user data matches the predefined user
    if (firstName === temporaryDatabase.user1.firstName &&
        lastName === temporaryDatabase.user1.lastName &&
        password === temporaryDatabase.user1.password) {
        // If the user information is correct, proceed to the homepage
        redirectToHomepage();
    } else {
        // If the user information is incorrect, show an alert
        alert('Incorrect user information. Please try again.');
    }
}

function saveUserInfo(firstName, lastName) {
    // Encrypt user information before storing (you can use more secure encryption algorithms)
    var encryptedFirstName = encryptData(firstName);
    var encryptedLastName = encryptData(lastName);

    // Save encrypted user information to local storage
    localStorage.setItem('encryptedFirstName', encryptedFirstName);
    localStorage.setItem('encryptedLastName', encryptedLastName);
}

function encryptData(data) {
    // Implement encryption logic (you can use libraries like CryptoJS for encryption)
    // For simplicity, let's assume encryption logic is implemented elsewhere
    return data; // Placeholder for encryption logic
}

const temporaryDatabase = {
    user1: {
        firstName: "Adi",
        lastName: "Akriv",
        password: "A12345678"
    }
};

function redirectToHomepage() {
    window.location.href = 'HomePage.html';
}

document.getElementById('loginForm').addEventListener('submit', handleFormSubmission);
