// document.addEventListener("DOMContentLoaded", function () {
//     let loginForm = document.querySelector("form");
//     if (loginForm) {
//         loginForm.addEventListener("submit", function(event) {
//             let username=document.querySelector("input[name='username']").value;
//             let password=document.querySelector("input[name='password']").value;

//             if (username.trim() === "" || password.trim() === "") {
//                 alert("Username and password cannot be empty!");
//                 event.preventDefault();
//             }
//         })
//     }
// })

document.addEventListener("DOMContentLoaded", function() {
    const inputs= document.querySelectorAll("input");
    inputs.forEach((input) => {
        input.addEventListener("focus", () => {
            input.style.borderColor="#e91e63";
        });
        input.addEventListener("blur", () => {
            input.style.borderColor= "#ccc";
        });
    });
});