#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(argv[2], (error, response, _body) => {
  console.error(error);
  console.log('code: ' + response.statusCode);
});
