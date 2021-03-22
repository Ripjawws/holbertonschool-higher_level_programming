#!/usr/bin/node
/*
Script that prints a square
*/
let a;
let b;
if ((a = process.argv[2]) && (b = parseInt(a))) {
  for (let i = 0; i < b; i++) {
    console.log('x'.repeat(b));
  }
} else {
  console.log('Missing size');
}
