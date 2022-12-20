#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(argv[2], (_error, _response, body) => {
  const data = JSON.parse(body);
  const result = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0
  };

  data.forEach((val) => {
    if (val.completed) {
      result[val.userId] += 1;
    }
  });

  console.log(result);
});
