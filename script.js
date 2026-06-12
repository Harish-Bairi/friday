// script.js

function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // ❌ No validation
    fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("msg").innerText = data.message;

        if (data.status === "success") {
            window.location.href = "home.html";
        }
    })
    .catch(err => {
        console.log(err); // ❌ Poor error handling
    });
}