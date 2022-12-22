#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${argv[2]}/`, (_error, _response, body) => {
  const data = JSON.parse(body);

  const characters = data.characters;

  characters.forEach((charUrl) => {
    request(charUrl, (_error, _response, info) => {
      const charData = JSON.parse(info);
      console.log(charData.name);
    });
  });
});
