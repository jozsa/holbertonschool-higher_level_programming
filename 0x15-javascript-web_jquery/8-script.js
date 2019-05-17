$(function () {
    $.ajax({
        type: 'GET',
        url: 'https://swapi.co/api/films/?format=json',
        success: function(films) {
            $.each(films.results, function(i, film) {
                    $("#list_movies").append("<li>"+ film.title +"</li>");
            });
        }
    });
});