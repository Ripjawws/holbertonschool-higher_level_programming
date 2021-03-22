#!/usr/bin/node
/*
Script that prints a square
*/
const a = parseInt(process.argv[2]);
if (isNaN(a) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < a; i++) {
    console.log('x'.repeat(a));
  }
}
