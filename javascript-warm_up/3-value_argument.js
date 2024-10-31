<<<<<<< HEAD
#!/usr/bin/node
const args = process.argv.slice(2);  // Get the arguments starting from the third one

if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
=======
#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
>>>>>>> afb2f6576bfb04b32db6c5c1ad7765100527f9b2
