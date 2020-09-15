"use strict";

$('.navTrigger').click(function () {
  $(this).toggleClass('active');
  console.log("Clicked menu");
  $("#mainListDiv").toggleClass("show_list");
  $("#mainListDiv").fadeIn();
});
$('.carousel').carousel({
  interval: 2000
});

if ($(window).width() < 900) {
  $('#aboutSection').removeClass('ml-auto');
  $('#aboutSection').removeClass('mr-auto');
}