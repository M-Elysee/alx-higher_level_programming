const h = $('header');
$('#toggle_header').on('click', function () {
  if (h.hasClass('green')) {
    h.removeClass('green');
    h.addClass('red');
  } else {
    h.remove('red');
    h.addClass('green');
  }
});
