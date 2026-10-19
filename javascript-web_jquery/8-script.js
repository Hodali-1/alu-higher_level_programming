$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $.each(data.results, function (index, film) {
    $('#list_movies').append($('<li></li>').text(film.title));
  });
});
