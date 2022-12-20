#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(argv[2], (_error, _response, body) => {
  const data = JSON.parse(body);
  const result = {};

  data.forEach((val) => {
    if (val.completed) {
      if (result[val.userId]) {
        result[val.userId] += 1;
      } else {
        result[val.userId] = 0;
      }
    }
  });

  console.log(result);
});
