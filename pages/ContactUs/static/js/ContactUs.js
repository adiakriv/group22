document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.form_container');
    const submitButton = document.querySelector('.submit-button');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        if (!name || !email || !message) {
            alert('Please fill in all fields.');
            return;
        }

        if (name.length > 50) {
            alert('Name must be up to 50 characters.');
            return;
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Please enter a valid email address.');
            return;
        }

        if (message.length > 500) {
            alert('Message should be no more than 500 characters.');
            return;
        }


        alert('Message sent successfully!');
        form.reset();
    });
});

localStorage.setItem('contactUs', 'sasaasassa')
localStorage.getItem('contactUs')
localStorage.removeItem('contactUs')