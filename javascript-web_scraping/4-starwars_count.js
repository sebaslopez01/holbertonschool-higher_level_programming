#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(argv[2], (_error, _response, body) => {
  const data = JSON.parse(body);

  const result = data.results.filter((val) => val.characters.includes('18'));

  console.log(result.length);
});
