function LongestWord(sen) {
  // code goes here
  const noSpecialChars = sen.replace(/[^a-zA-Z0-9 ]/g, "");

  sen = noSpecialChars.split(" ");

  sen.sort(function (a, b) {
    return b.length - a.length;
  });

  return sen[0];
}

// keep this function call here
console.log(LongestWord(readline()));

// Longest Word
// Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string.
// If there are two or more words that are the same length, return the first word from the string with that length.
//Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
// Examples
// Input: "fun&!! time"
// Output: time
// Input: "I love dogs"
// Output: love
