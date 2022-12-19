#!/usr/bin/node

const { argv } = require('process');

const number = parseInt(argv[2]);

if (!number) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
}
