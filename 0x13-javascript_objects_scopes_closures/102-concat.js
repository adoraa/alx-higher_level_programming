#!/usr/bin/node
const fs = require('fs');

const [, , fileA, fileB, fileC] = process.argv;

const fa = fs.readFileSync(fileA, 'utf8');
const fb = fs.readFileSync(fileB, 'utf8');

const concatContent = fa + fb;

fs.writeFileSync(fileC, concatContent);
