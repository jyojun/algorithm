const fs = require("fs");
let input = fs.readFileSync("./stdin/3-2").toString().split("\n");

function solution(input) {
  let n, m, k;
  let result = 0;
  let info = input[0].split(" ").map((d) => parseInt(d));
  let nums = input[1].split(" ").map((d) => parseInt(d));

  n = info[0];
  m = info[1];
  k = info[2];

  // nums 내림 차순으로 정렬
  nums.sort((a, b) => b - a);

  // 가장 큰 값, 두번째로 큰값 저장
  first = nums[0];
  second = nums[1];
  cnt = 0;
  // k번 연속으로 더하면 안됨
  for (let i = 0; i < m; i++) {
    if (cnt >= k) {
      result += second;
      cnt = 0; // 연속으로 더한 횟수 초기화 후 두번째로 큰값을 더함
      continue;
    }
    result += first;
    cnt++;
  }

  return result;
}

console.log(solution(input));
