$('document').ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const code = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://hellosalut.stefanbohacek.dev/?cc=' + code,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
