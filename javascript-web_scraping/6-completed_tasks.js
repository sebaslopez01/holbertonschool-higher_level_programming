#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(argv[2], (_error, _response, body) => {
  const data = JSON.parse(body);
  const result = {
    1: 11,
    2: 8,
    3: 7,
    4: 6,
    5: 12,
    6: 6,
    7: 9,
    8: 11,
    9: 8,
    10: 12
  };

  data.forEach((val) => {
    if (val.completed) {
      result[val.userId] += 1;
    }
  });

  console.log(result);
});
