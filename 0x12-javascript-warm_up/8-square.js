#!/usr/bin/node
const value = 'x';
const myArg = parseInt(process.argv[2]);
if (!isNaN(myArg)) {
  for (let i = 1; i <= myArg; i++) {
    console.log(value.repeat(myArg));
  }
} else {
  console.log('Missing size');
}
