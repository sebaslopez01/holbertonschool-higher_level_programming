#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((typeof w !== 'number' || w <= 0) || (typeof h !== 'number' || h <= 0)) {
      return;
    }

    this.width = w;
    this.height = h;
  }
}

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);
