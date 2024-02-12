#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};
console.log(parseInt(factorial(process.argv[2])));
