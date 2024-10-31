#!/usr/bin/node

// Recursive function to compute factorial
function factorial (n) {
  if (isNaN(n)) return 1; // Factorial of NaN is 1
  if (n <= 1) return 1; // Base case: factorial of 0 or 1 is 1
  return n * factorial(n - 1); // Recursive case
}

// Get the first argument, cast it to integer
const arg = parseInt(process.argv[2]);

// Print the factorial result
console.log(factorial(arg));
