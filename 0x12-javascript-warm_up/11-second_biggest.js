#!/usr/bin/node

function secondBiggest (arr) {
  arr.sort((a, b) => b - a);
  return arr[1] || 0;
}

const argList = process.argv.slice(2);
const intArgs = argList.map(arg => parseInt(arg));
const res = secondBiggest(intArgs);

console.log(res);
