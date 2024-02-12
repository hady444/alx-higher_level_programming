#!/usr/bin/node
const { argv } = require('process');
let n1 = 0;
let n2 = 0;
let tmp = 0;
if (argv.length <= 3) {
  console.log(0);
} else {
  if (parseInt(argv[2]) > parseInt(argv[3])) {
    n1 = parseInt(argv[2]);
    n2 = parseInt(argv[3]);
  } else {
    n1 = parseInt(argv[3]);
    n2 = parseInt(argv[2]);
  }
  for (let i = 4; i < argv.length; i++) {
    if (n1 < parseInt(argv[i])) {
      tmp = n1;
      n1 = parseInt(argv[i]);
      n2 = tmp;
    } else if (n2 < parseInt(argv[i])) {
      n2 = parseInt(argv[i]);
    }
  }
  console.log(n2);
}
