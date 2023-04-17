#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const row = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Rectangle;
