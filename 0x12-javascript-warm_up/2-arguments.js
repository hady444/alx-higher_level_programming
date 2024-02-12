#!/usr/bin/node
const { argv } = require('node:process');
let l = argv.length - 2;
if (l === 1) {
  console.log('Argument found');
} else if (l === 0) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
