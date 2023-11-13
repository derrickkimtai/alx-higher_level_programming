#!/usr/bin/node
const numArgs = process.argv.lenght;

if (numArgs === 2){
    console.log("No argument");
}
 else if (numArgs === 3){
	 console.log("Argument found");
 }
else{
	console.log("Arguments found");
}
