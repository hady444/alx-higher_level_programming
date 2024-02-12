#!/usr/bin/node
function factorial (num) {
  if (num === 1 || !(num)) {
    return (1);
  }
  return (num * factorial(num - 1));
}
console.log(parseInt(factorial(process.argv[2])));
