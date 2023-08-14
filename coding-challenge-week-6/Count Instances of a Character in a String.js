//  Create a function that takes two strings as arguments and returns the number of times the
//first string (the single character) is found in the second string.

// Examples
// charCount("a", "edabit") ➞ 1

// charCount("c", "Chamber of secrets") ➞ 1

// charCount("b", "big fat bubble") ➞ 4
// Notes
// Your output must be case-sensitive (see second example).

function charCount(a, b) {
  let sum = 0;
  let bArr = b.split("");

  for (let i = 0; i < bArr.length; i++) {
    if (bArr[i] === a) {
      sum++;
    }
  }

  return sum;
}

console.log(charCount("c", "Chamber of secrets"));
console.log(charCount("b", "big fat bubble"));
