#!/usr/bin/node
const args = process.argv.slice(2);  // Get command line arguments

if (args[0] !== undefined && !isNaN(args[0])) {
  const num = parseInt(args[0]);
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
