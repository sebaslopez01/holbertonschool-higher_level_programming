#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${argv[2]}`, (_error, _response, body) => {
  const data = JSON.parse(body);

  console.log(data.title);
});
