const password = document.getElementById('password');
const confirmPassword = document.getElementById('confirm_password');
const submitButton = document.getElementById('submit-button');

const valid = element => {
    element.classList.remove('invalid');
    element.classList.add('valid');
}

const invalid = element => {
    element.classList.remove('valid');
    element.classList.add('invalid');
}

const clearValidation = element => {
    element.classList.remove('valid');
    element.classList.remove('invalid');
}

const enableButton = () => {
    if (password.classList.contains('valid') &&
        confirmPassword.classList.contains('valid')) {
        submitButton.disabled = false;
    } else {
        submitButton.disabled = true;
    }
}

const validateInputs = () => {

    // Check Length Of Password
    if (password.value.length < 8) {
        invalid(password);
    } else {
        valid(password);
    }

    // Check Length Of Confirm Password
    if (confirmPassword.value.length < 8) {
        invalid(confirmPassword)
    } else {
        valid(confirmPassword)
    }

    // Check If Password & Check Password Match
    if (confirmPassword.value != password.value) {
        invalid(confirmPassword);
    } else {
        valid(confirmPassword);
    }

    // Clears Validation If Password Empty
    if (password.value == '') {
        clearValidation(password);
    }

    // Clears Validation If Check Password Empty
    if (confirmPassword.value == '') {
        clearValidation(confirmPassword);
    }

    enableButton();

}

password.addEventListener('keyup', validateInputs)
confirmPassword.addEventListener('keyup', validateInputs)