#!/usr/bin/node
/*
Prints if its number
*/
let num = 0;
num = parseInt(process.argv[2]);
if (num) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
