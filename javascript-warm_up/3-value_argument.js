#!/usr/bin/node
const args = process.argv.slice(2);  // Get the arguments starting from the third one

if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
