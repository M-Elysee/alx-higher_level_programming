$('document').ready(function () {
  $('div#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').on('click', function () {
    $('UL.my_list li:last').remove();
  });
  $('div#clear_list').on('click', function () {
    $('UL.my_list').empty();
  });
});
