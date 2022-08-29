const fs = require("fs");
let input = fs.readFileSync("./stdin/4-1").toString().split("\n");

function checkLoc(N, loc) {
  if (loc[0] > 0 && loc[0] < N && loc[1] > 0 && loc[1] < N) return true;
  return false;
}
function move(loc, dir) {
  let result = [...loc]; // 얕은 복사를 해야 solution 함수에서 두번 움직이는 에러가 나지 않는다.
  if (dir === "L") {
    result[1]--;
  } else if (dir === "R") {
    result[1]++;
  } else if (dir === "U") {
    result[0]--;
  } else if (dir === "D") {
    result[0]++;
  }
  return result;
}
function solution(input) {
  let loc = [1, 1];
  let N = parseInt(input[0]);
  let moveList = input[1].split(" ");

  for (let i = 0; i < moveList.length; i++) {
    if (checkLoc(N, move(loc, moveList[i]))) {
      loc = move(loc, moveList[i]);
    }
  }

  console.log(loc[0], loc[1]);
}

solution(input);
