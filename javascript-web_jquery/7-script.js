#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/people/5/?format=json', (_error, _response, body) => {
  const data = JSON.parse(body);

  $('#character').html(data.name);
});
