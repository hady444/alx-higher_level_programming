#!/usr/bin/node
const arr = require('./100-data.js').list;
console.log(arr.map((x, i) => x * i));
