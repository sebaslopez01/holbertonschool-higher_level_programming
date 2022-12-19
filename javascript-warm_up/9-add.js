#!/usr/bin/node

const { argv } = require('process');

const firstNumber = parseInt(argv[2]);
const secondNumber = parseInt(argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(firstNumber, secondNumber);
