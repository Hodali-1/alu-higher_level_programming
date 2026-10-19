#!/usr/bin/node
const Square = require('./5-square');

class MySquare extends Square {
  charPrint (c) {
    const ch = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += ch;
      }
      console.log(row);
    }
  }
}

module.exports = MySquare;
