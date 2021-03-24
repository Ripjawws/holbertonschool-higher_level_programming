#!/usr/bin/node
/*

*/
const Square5 = require('./5-square');
class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 1; i <= this.height; i++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
