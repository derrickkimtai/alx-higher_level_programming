#!/usr/bin/node
const myArg = parseInt(process.argv[2]);
if (!isNaN(myArg)) {
  for (let i = 1; i <= myArg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
