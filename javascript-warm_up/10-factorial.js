#!/usr/bin/node

const { argv } = require('process');

const firstNumber = parseInt(argv[2]) || 1;

function factorial (n) {
  if (n <= 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

console.log(factorial(firstNumber));
