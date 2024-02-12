#!/usr/bin/node
const { argv } = require('process');
const num = parseInt(argv[2]);
if (Number.isInteger(num)) {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
