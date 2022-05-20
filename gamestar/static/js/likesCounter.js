likeButtons = document.getElementsByClassName('like-btn')

for (const likeButton of likeButtons) {
    likeButton.addEventListener('click', e => {
        e.target.children[0].classList.toggle('liked')

        const formData = new FormData();
        formData.append("review_id", e.target.dataset.reviewId);

        const xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                // const data = JSON.parse(xhttp.responseText)
                console.log(xhttp.responseText)
                likeButton.children[1].innerText = xhttp.responseText
                // console.log(data)
            }
        };

        xhttp.open("POST", "/likes", true);
        xhttp.send(formData);
        likeButton.disabled = true
    })
}