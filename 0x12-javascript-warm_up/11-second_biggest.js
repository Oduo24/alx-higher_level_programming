#!/usr/bin/node
const arg = process.argv.slice(2);
if (arg.length === 0 || arg.length === 1) {
  console.log('0');
}

function toInt (a) {
  return parseInt(a);
}

const newList = arg.map(toInt);
const sortedList = newList.sort(function (a, b) { return a - b; });
console.log(sortedList[1]);
