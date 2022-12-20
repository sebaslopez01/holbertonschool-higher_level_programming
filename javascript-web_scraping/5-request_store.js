#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');
const request = require('request');

request(argv[2], (_error, _response, body) => {
  fs.writeFileSync(argv[3], body);
});
