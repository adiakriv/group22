

document.addEventListener("DOMContentLoaded", function () {
    const formFields = document.querySelectorAll('.form_container input');

    formFields.forEach(function (field) {
        field.disabled = true;
    });

    const star3 = document.getElementById('star3');
    star3.checked = true;
});

document.addEventListener("DOMContentLoaded", function () {
    var profileContainer = document.querySelector('.profile-container');

    var body = document.querySelector('body');

    var numberOfCopies = 3;

    for (var i = 0; i < numberOfCopies; i++) {
        var clone = profileContainer.cloneNode(true);

        body.appendChild(clone);
    }

});

