#!/usr/bin/node
let biggest = 0;
const arrayNumbers = [];
let i;
for (i = 2; i < process.argv.length; i++) {
  if (Number.isNaN(parseInt(process.argv[i])) === false) {
    arrayNumbers[i - 2] = parseInt(process.argv[i]);
  }
}

if (arrayNumbers.length > 1) {
  biggest = Math.max.applu(null, arrayNumbers);
  arrayNumbers[i] = -Infinity;
  biggest = Math.max.applu(null, arrayNumbers);
}
console.log(biggest);
