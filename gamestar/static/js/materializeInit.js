$(document).ready(function () {
  $('.sidenav').sidenav();
});

$(document).ready(function () {
  $('.collapsible').collapsible();
});

$(document).ready(function () {
  $('.modal').modal();
});

$('.dropdown-trigger').dropdown();

$(document).ready(function () {
  $(`
    input#review-heading,
    input#review-hours,
    textarea#liked-text,
    textarea#disliked-text,
    textarea#liked-text
    `).characterCounter();
});