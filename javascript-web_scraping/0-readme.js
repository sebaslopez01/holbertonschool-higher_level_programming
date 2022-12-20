#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

const buff = fs.readFileSync(argv[2]);

console.log(buff.toString('utf-8'));
