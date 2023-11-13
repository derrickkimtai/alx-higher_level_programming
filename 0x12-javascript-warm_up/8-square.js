#!/usr/bin/node
const myArg = parseInt(process.argv[2]);
if (!isNaN(myArg)) {
  for (let i = 1; i <= myArg; i++) {
    console.log('x'.repeat(myArg));
  }
} else {
  console.log('Missing size');
}
