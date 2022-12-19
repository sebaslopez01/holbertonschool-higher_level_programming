#!/usr/bin/node

const { argv } = require('process');

const arg = argv.slice(2);
console.log(arg[0] || 'No argument');
