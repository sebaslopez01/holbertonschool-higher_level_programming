#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(argv[2], (_error, response, _body) => {
  console.log('code: ' + response.statusCode);
});
