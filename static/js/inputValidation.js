$("#password").on('focusout', e =>{
    if (e.target.value === '') {
        return $("#confirm_password")
        .removeClass("valid")
        .removeClass("invalid");
    }

    if (e.target.value != $("#confirm_password").val()) {
        $("#confirm_password")
        .removeClass("valid")
        .addClass("invalid");
    } else {
        $("#confirm_password")
        .removeClass("invalid")
        .addClass("valid");
    }
});

$("#confirm_password").on('focusout', e =>{
    if ($("#password").val() === '') {
        return $("#confirm_password")
        .removeClass("valid")
        .removeClass("invalid");
    }

    if (e.target.value != $("#password").val()) {
        $('#confirm_password')
        .removeClass("valid")
        .addClass("invalid");
    } else {
        $('#confirm_password')
        .removeClass("invalid")
        .addClass("valid");
    }
})