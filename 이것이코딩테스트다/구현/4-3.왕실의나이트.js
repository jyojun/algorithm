const fs = require("fs");
let input = fs.readFileSync("./stdin/4-3").toString();
function checkLoc(loc, step) {
  let curr = [loc[0] + step[0], loc[1] + step[1]];
  if (curr[0] > 0 && curr[0] <= 8 && curr[1] > 0 && curr[1] <= 8) return true;
  return false;
}
function solution(input) {
  let col = parseInt(input[1]);
  let row = input.charCodeAt(0) - "a".charCodeAt(0) + 1;
  let loc = [row, col];
  let steps = [
    [-1, 2],
    [1, 2],
    [2, 1],
    [2, -1],
    [1, -2],
    [-1, -2],
    [-2, -1],
    [-2, 1],
  ];
  let cnt = 0;
  for (const s of steps) {
    if (checkLoc(loc, s)) cnt++;
  }
  console.log(cnt);
}

solution(input);
