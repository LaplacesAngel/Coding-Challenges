// Create a function that finds the maximum range of a triangle's third edge, 
//where the side lengths are all integers.

// Examples
// nextEdge(8, 10) ➞ 17

// nextEdge(5, 7) ➞ 11

// nextEdge(9, 2) ➞ 10

function nextEdge (s1, s2) {
    let s3 = s1 + s2 -1
    return s3;
}

console.log(nextEdge(8, 10));