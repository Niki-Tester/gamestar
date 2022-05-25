const likeButtons = document.getElementsByClassName('like-btn');

let gAwaitingResult = false;

for (const likeButton of likeButtons) {
    likeButton.addEventListener('click', toggleLike);
}

function toggleLike(e) {
    e.preventDefault();
    const likeCounter = document.getElementById(`review-counter-${e.target.dataset.reviewId}`);

    const formData = new FormData();
    formData.append("review_id", e.target.dataset.reviewId);

    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            e.target.children[0].classList.toggle('liked');
            e.target.children[1].innerText = xhttp.responseText;
            likeCounter.innerText = xhttp.responseText;
            gAwaitingResult = false;
        }
    };

    if (!gAwaitingResult) {
        gAwaitingResult = true;
        xhttp.open("POST", "/likes", true);
        xhttp.send(formData);
    } else {
        console.log('Awaiting Previous Response');
    }
}