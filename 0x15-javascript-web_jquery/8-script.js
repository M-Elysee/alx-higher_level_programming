$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (films) {
    $.each(films.results, function (i, film) {
      const item = $('<li></li>').text(film.title);
      $('UL#list_movies').append(item);
    });
  },
  error: function (e) {
    console.log(e);
  }
});
