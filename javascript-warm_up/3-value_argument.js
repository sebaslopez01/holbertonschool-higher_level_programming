#!/usr/bin/node

const { argv } = require('process');

const arg = argv.slice(2);
console.log(arg.toString().replace(',', ' ') || 'No argument');
