#!/usr/bin/node
const args = process.argv.slice(2);
const sortedArgs = args.sort((a, b) => b - a);
const secondBiggest = sortedArgs[1] || 0;
console.log(secondBiggest);