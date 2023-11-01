$('document').ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    translate();
  });
  $('INPUT#language_code').on('keypress', function (e) {
    if (e.which === 13) { translate(); }
  });
  function translate () {
    const code = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://hellosalut.stefanbohacek.dev/?cc=' + code,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  }
});
