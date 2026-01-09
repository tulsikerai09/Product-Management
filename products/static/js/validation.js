// LOGIN VALIDATION
function validateLoginForm() {
    const username = document.getElementById("login-username").value.trim();
    const password = document.getElementById("login-password").value.trim();

    if (username === "" || password === "") {
        alert("Both username and password are required.");
        return false;
    }
    return true;
}

// REGISTER VALIDATION
function validateRegisterForm() {
    const username = document.getElementById("reg-username").value.trim();
    const password = document.getElementById("reg-password").value.trim();

    if (username.length < 3) {
        alert("Username must be at least 3 characters long.");
        return false;
    }

    if (password.length < 6) {
        alert("Password must be at least 6 characters long.");
        return false;
    }

    return true;
}

// PRODUCT VALIDATION
function validateProductForm() {
    const name = document.getElementById("product-name").value.trim();
    const price = document.getElementById("product-price").value.trim();

    if (name === "") {
        alert("Product name is required.");
        return false;
    }

    if (price === "" || price <= 0) {
        alert("Enter a valid product price.");
        return false;
    }

    return true;
}
