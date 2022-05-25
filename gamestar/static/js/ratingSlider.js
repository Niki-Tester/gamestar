const slider = document.getElementById('review-rating');
slider.addEventListener('input', updateRating);

const rating_inner = document.querySelector('.rating-inner');

function updateRating() {
    rating_inner.style.width = `${Math.round(mapNum(slider.value, 0, 5, 0, 100))}%`;
}

function mapNum(number, inMin, inMax, outMin, outMax) {
    return (number - inMin) * (outMax - outMin) / (inMax - inMin) + outMin;
}

document.addEventListener('DOMContentLoaded', () => {
    updateRating();
});