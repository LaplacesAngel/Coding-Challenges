// Create a function that takes two strings as arguments and returns the number of 
//times the first string (the single character) is found in the second string.

// Examples
// charCount("a", "edabit") ➞ 1

// charCount("c", "Chamber of secrets") ➞ 1

// charCount("b", "big fat bubble") ➞ 4


//takes two strings as arguments

const charCount = (a,b) => {
    let count = 0;

    let bArr = b.split("")

    for (let i = 0; i < bArr.length; i++ ) {
        if(a === bArr[i]) {
            count ++;
        }
    }
    return count;
}

console.log(charCount("b", "big fat bubble"));