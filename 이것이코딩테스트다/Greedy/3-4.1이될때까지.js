const fs = require("fs");
let input = fs.readFileSync("./stdin/3-4").toString().split("\n");

function solution(input) {
  let n, k;
  let info = input[0].split(" ").map((d) => parseInt(d));
  n = info[0];
  k = info[1];
  let cnt = 0;

  // target 이 1이 될 때까지 반복
  let target = parseInt(n / k) * k;
  while (n > 1) {
    target = parseInt(n / k) * k;
    // target과 같을 경우
    if (n === target) {
      n /= k;
      cnt++; // 한번만 추가
    } else {
      cnt += n - target;
      n = target;
    }
  }

  console.log(cnt + (n - 1));
}

solution(input);
