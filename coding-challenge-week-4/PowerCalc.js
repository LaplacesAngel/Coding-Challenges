// problem URL https://edabit.com/challenge/wAdE9te55cowBLcPs

function addUp(number) {
  let sum = 0;
  for (let i = 0; i <= number; i++) {
    sum += i;
  }
  return sum;
}

console.log(addUp(600));
