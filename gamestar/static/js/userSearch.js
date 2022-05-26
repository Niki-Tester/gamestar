const searchInput = document.getElementById('search-input')
const userCards = document.getElementsByClassName('searchable');

searchInput.addEventListener('keyup', e => {
    const searchQuery = e.target.value.toLowerCase();

    for (const userCard of userCards) {
        const username = userCard.firstElementChild.textContent.toLowerCase();
        if (!username.includes(searchQuery)) {
            userCard.parentElement.parentElement.classList.add('hide')
        } else {
            userCard.parentElement.parentElement.classList.remove('hide')
        }
    }
})