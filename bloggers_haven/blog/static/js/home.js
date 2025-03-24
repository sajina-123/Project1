document.addEventListener("DOMContentLoaded", function() {
    let logoutButton=document.querySelector("button");

    logoutButton.addEventListener("click", function(event) {
        event.preventDefault();

        let confirmLogout=confirm("Are you sure want to logout?");
        if (confirmLogout) {
            window.location.href = logoutButton.parentElement.href;
        }
    });
});