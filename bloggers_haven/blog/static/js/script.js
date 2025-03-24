document.addEventListener("DOMContentLoaded", function () {
    let form=document.querySelector("form");
    form.addEventListener("submit", function(event) {
        let username=document.querySelector("input[name='username']").value;
        let password=document.querySelector("input[name='password']").value;

        if(username.trim()=== "" || password.trim() ==="") {
            alert("All fields are required!");
            event.preventDefault();
        }
    });
});