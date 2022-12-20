#!/usr/bin/node

$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  type: 'GET',
  dataType: 'json'
}).done((data) => {
  const movies = data.results;

  const listMovies = $('#list_movies');

  movies.forEach((val) => {
    listMovies.append(`<li>${val.title}</li>`);
  });
});
