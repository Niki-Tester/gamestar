const searchInput = document.getElementById('search-game');
const results = document.getElementById('results');
let typingTimer;
let doneTypingInterval = 600;

searchInput.addEventListener('submit', submitForm);

/* 
Listens for keyup, starts time out to prevent searching while user completes
search query.
*/
searchInput.addEventListener('keyup', () => {
    clearTimeout(typingTimer);
    typingTimer = setTimeout(submitForm, doneTypingInterval);
});

function submitForm() {

    // Clears previously received results
    results.innerHTML = '';

    // Clears results when search input is empty
    if (searchInput.value.length == 0) {
        return results.innerHTML = '';
    }

    // Provides user feedback if search query is less than 3 characters
    if (searchInput.value.length < 3) {
        return results.innerHTML = '<p>Enter a minimum of 3 characters to search</p>';
    }

    // Displays loading animation while waiting for API response
    const loader = document.getElementById('loader');
    loader.classList.remove('hide');

    const formData = new FormData();
    formData.append("search", searchInput.value.trim());

    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // Hides loading animation as response received from API
            loader.classList.add('hide');
            const data = JSON.parse(xhttp.responseText);
            displayResults(data);
        }
    };

    xhttp.open("POST", "/search");
    xhttp.send(formData);
}

function displayResults(data) {

    // Clears previously received results
    results.innerHTML = '';

    // User feedback when no results found from API
    if (data.length === 0) {
        return results.innerHTML = `<p>Game Not Found!</p>`;
    }

    const ul = document.createElement('ul');

    // Creates required elements for each result received from the API
    for (let i = 0; i < data.length; i++) {

        const divHeader = document.createElement('div');
        divHeader.setAttribute('class', 'collapsible-header grey darken-3 amber-text text-lighten-1');

        const gameName = document.createElement('h6');
        gameName.setAttribute('class', 'text-shadow');
        gameName.textContent = data[i].name;

        const icon = document.createElement('i');
        icon.setAttribute('class', 'fa-solid fa-caret-down');
        icon.after(gameName);

        divHeader.append(gameName);
        divHeader.append(icon);

        const divBody = document.createElement('div');
        divBody.setAttribute('class', 'collapsible-body grey darken-4');

        const divBodyInner = document.createElement('div');
        divBodyInner.setAttribute('class', 'row');

        const gameImage = document.createElement('img');
        gameImage.src = data[i].img_url;
        gameImage.setAttribute('class', 'col hide-on-small-only m4 l3');

        const gameSummary = document.createElement('p');
        if (data[i].summary == undefined) data[i].summary = 'No Game Summary Found!';
        gameSummary.innerText = data[i].summary;
        gameSummary.setAttribute('class', 'white-text col s12 m8 l9');

        const hiddenInput = document.createElement('input');
        hiddenInput.setAttribute('class', 'hide');
        hiddenInput.setAttribute('type', 'number');
        hiddenInput.setAttribute('id', 'game_id');
        hiddenInput.setAttribute('name', 'game_id');
        hiddenInput.setAttribute('value', data[i].id);

        const addReviewLink = document.createElement('a');
        addReviewLink.innerText = 'Add Review';
        addReviewLink.setAttribute('class', 'btn waves-effect waves-light green darken-4');
        addReviewLink.href = data[i].anchor_href;

        divBodyInner.append(gameImage);
        divBodyInner.append(addReviewLink);
        divBodyInner.append(gameSummary);
        divBody.append(divBodyInner);


        const li = document.createElement('li');
        li.append(divHeader);
        li.append(divBody);
        ul.append(li);
    }

    ul.setAttribute('class', 'collapsible');
    results.append(ul);

    // Initializes collapsible element from Materialize CSS
    $('.collapsible').collapsible();

    const loading = e => {

        const wrapper = document.createElement('div');
        wrapper.setAttribute('class', 'preloader-wrapper small active');

        const spinner = document.createElement('div');
        spinner.setAttribute('class', 'spinner-layer spinner-white-only');

        const circleLeft = document.createElement('div');
        circleLeft.setAttribute('class', 'circle-clipper left');

        const gap = document.createElement('div');
        gap.setAttribute('class', 'gap-patch');

        const circleRight = document.createElement('div');
        circleRight.setAttribute('class', 'circle-clipper right');

        const circle = document.createElement('div');
        circle.setAttribute('class', 'circle');

        circleLeft.append(circle);
        gap.append(circle);
        circleRight.append(circle);

        spinner.append(circleLeft, gap, circleRight);

        wrapper.append(spinner);

        e.currentTarget.replaceWith(wrapper);
    };

    const links = document.getElementsByClassName('btn');
    for (const link of links) {
        link.addEventListener('click', loading);
    }
}

// Clear search results / search input if user returns to page using back button
(() => {
    window.onpageshow = e => {
        if (e.persisted) {
            results.innerHTML = '';
            searchInput.value = '';
        }
    };
})();