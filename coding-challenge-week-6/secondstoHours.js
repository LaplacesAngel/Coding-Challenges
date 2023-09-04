// Convert Hours into Seconds
// Write a function that converts hours into seconds.

// Examples
// howManySeconds(2) ➞ 7200

// howManySeconds(10) ➞ 36000

// howManySeconds(24) ➞ 86400


const howManySeconds = (n) => {
   n = n * 60 * 60;
   return n;
}

console.log(howManySeconds(24));