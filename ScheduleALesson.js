document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('.form_container');
    const dateInput = document.getElementById('date');
    const submitButton = document.querySelector('.submit-button');

    function validateDate(dateString) {
        const selectedDate = new Date(dateString);
        const currentDate = new Date();
        const threeMonthsLater = new Date();
        threeMonthsLater.setMonth(currentDate.getMonth() + 3);

        if (selectedDate > threeMonthsLater) {
            alert("Please select a date within the next 3 months.");
            return false;
        }

        if (selectedDate <= currentDate) {
            alert("Please select a date in the future.");
            return false;
        }

        return true;
    }

    function handleFormSubmission(event) {
        event.preventDefault();

        const selectedDate = dateInput.value;

        if (!selectedDate) {
            alert("No date selected, please try again.");
            return;
        }

        if (!validateDate(selectedDate)) {
            return;
        }

        alert("The lesson has been set successfully");
        window.location.href = "HomePage.html"; //s
    }

    submitButton.addEventListener('click', handleFormSubmission);
});
