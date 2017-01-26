// from -10 to 19
for (var i = -10; i < 20; i++) {
  console.log(i);
}

// from 10 to 40 even
for (var i = 10; i < 41; i+=2) {
  console.log(i);
}

//300 - 333 odd
for (var i = 301; i < 334; i+=2) {
  console.log(i);
}

//print all # divisible by 5 AND 3    (range 5-50)
for (var i = 5; i < 51; i++) {
  if (i%5 === 0 && i%3 === 0) {
    console.log(i);
  }
}
