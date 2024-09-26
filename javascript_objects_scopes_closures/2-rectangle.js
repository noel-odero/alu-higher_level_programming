#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) {
            // Only initialize the width and height if both are positive integers
            this.width = w;
            this.height = h;
        }
        // Otherwise, an empty object is created by not initializing any properties
    }
}

module.exports = Rectangle;

