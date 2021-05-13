$(function() {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data){
        $.each(data.results, function (i, element){
            $('ul#list_movies').append('<li>' + element.title + '</li>');
        })
    })
});