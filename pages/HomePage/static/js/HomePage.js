
function handleLogout() {
    sessionStorage.removeItem('loggedIn');
    sessionStorage.removeItem('firstName');
    sessionStorage.removeItem('lastName');

    window.location.href = 'BookALesson.html';
}

document.addEventListener('DOMContentLoaded', function () {
    const logoutButton = document.querySelector('.click_me-button');

    logoutButton.addEventListener('click', handleLogout);
});
