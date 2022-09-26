const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  input.push(line);
});

rl.on("close", () => {
  let answer = [];
  let n = parseInt(input[0]);
  let parts = input[1].split(" ").map((p) => parseInt(p));
  let req = parseInt(input[2]);
  let req_parts = input[3].split(" ").map((r) => parseInt(r));

  parts.sort((a, b) => a - b);

  for (let part of req_parts) {
    let exist = binary_search(parts, part, 0, n - 1);
    if (exist) answer.push("yes");
    else answer.push("no");
  }

  console.log(answer.join(" "));
  process.exit();
});

function binary_search(array, target, start, end) {
  while (start <= end) {
    let mid = parseInt((start + end) / 2);

    if (array[mid] === target) return mid;
    else if (array[mid] > target) end = mid - 1;
    // target보다 크면 왼쪽에서 탐색
    else start = mid + 1; // target보다 작으면 오른쪽에서 탐색
  }
  return false;
}
