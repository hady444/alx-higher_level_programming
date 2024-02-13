#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  const len = list.length;
  for (let i = len - 1; i > -1; i--) {
    rev[len - i - 1] = list[i];
  }
  return rev;
};
