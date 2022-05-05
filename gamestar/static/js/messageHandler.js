messages = document.querySelectorAll('.flash');

if (messages) {
    messages.forEach(message => {
        message.addEventListener('click', e => {
            e.currentTarget.remove()
        })
    })
}