function FirstReverse(str) {
  arr = str.split("");
  let revArr = arr.reverse();
  str = revArr.join("");

  return str;
}

console.log(FirstReverse("Paul"));

//results url https://www.coderbyte.com/results/kjdkfjdakjfdjfdsakfjd:First%20Reverse:JavaScript
