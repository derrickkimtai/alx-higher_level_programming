#!/usr/bin/node
const numArgs = process.argv.lenght - 2;

if (numArgs === 1){
    console.log("No argument");
}
 else if (numArgs === 2){
	 console.log("Argument found");
 }
else{
	console.log("Arguments found");
}
