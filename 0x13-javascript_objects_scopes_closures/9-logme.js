#!/usr/bin/node
/*

*/

let numArguments = 0;
exports.logMe = (item) => {
  console.log(`${numArguments}: ${item}`);
  numArguments++;
}
