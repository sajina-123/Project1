document.addEventListener("DOMContentLoaded", function () {
    let loginForm = document.querySelector("form");
    if (loginForm) {
        loginForm.addEventListener("submit", function(event) {
            let username=document.querySelector("input[name='username']").value;
            let password=document.querySelector("input[name='password']").value;

            if (username.trim() === "" || password.trim() === "") {
                alert("Username and password cannot be empty!");
                event.preventDefault();
            }
        })
    }
})