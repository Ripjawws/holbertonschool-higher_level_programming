#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/*
Create an object Square
*/
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
