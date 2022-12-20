#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/?format=json', (_error, _response, body) => {
  const data = JSON.parse(body);
  const movies = data.results;

  const listMovies = $('#list_movies');

  movies.forEach((val) => {
    listMovies.append(val.title);
  });
});
