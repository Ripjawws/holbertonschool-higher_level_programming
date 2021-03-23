#!/usr/bin/node
/*
Create an object Triangle
*/
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (this.width <= 0 || this.height <= 0 || this.width === undefined || this.height === undefined) {
      const R = require('./0-rectangle.js');
      const b = new R();
      return b;
    }
  }
}
module.exports = Rectangle;
