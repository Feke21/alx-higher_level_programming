#!/usr/bin/node
const arr = process.argv.slice(2);

function secondBiggest (array) {
  let res;
  if (array.length === 0 || array.length === 1) {
    return (0);
  } else {
    array.sort((a, b) => b - a);
    array.shift();
    res = array.shift();
    return (res);
  }
}
const res = secondBiggest(arr);
console.log(res);
