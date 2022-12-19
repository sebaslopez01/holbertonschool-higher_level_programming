#!/usr/bin/node

const { argv } = require('process');

if (argv.length === 2 || argv.length === 3) {
  console.log('0');
} else {
  const arr = argv.slice(2).map((val) => parseInt(val));
  arr.sort((a, b) => a - b);
  const lastVal = arr.pop();
  const arr2 = arr.filter((val) => val !== lastVal);

  console.log(arr2.pop());
}
