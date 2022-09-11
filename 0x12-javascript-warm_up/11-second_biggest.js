#!/usr/bin/node
if (process.argv.length === 2) {
  console.log(`0`);
}else if (process.argv.length === 3) {
  console.log(`0`);
}

function toInt (a) {
  return parseInt(a);
}

const newList = process.argv.map(toInt);
const sortedList = newList.sort(function (a, b) { return a - b; });
console.log(sortedList[1]);
