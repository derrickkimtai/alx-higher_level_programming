#!/usr/bin/node
const firstArgs = process.argv[2];
if (!firstArgs) {
  console.log('No argument');
} else {
  console.log(firstArgs);
}
