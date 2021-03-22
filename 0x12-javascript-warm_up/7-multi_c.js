#!/usr/bin/node
/*
Script that prints x times “C is fun”
*/
let times = process.argv[2];
const repeated = 'C is fun';
while (times > 0) {
  console.log(repeated);
  times--;
}
