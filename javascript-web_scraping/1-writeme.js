#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

fs.writeFileSync(argv[2], argv[3]);
