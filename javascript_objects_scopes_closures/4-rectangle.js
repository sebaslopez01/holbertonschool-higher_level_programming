#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((typeof w !== 'number' || w <= 0) || (typeof h !== 'number' || h <= 0)) {
      return;
    }

    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tempVal = this.width;
    this.width = this.height;
    this.height = tempVal;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
