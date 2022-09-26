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
  let n = parseInt(input[0].split(" ")[0]);
  let target = parseInt(input[0].split(" ")[1]);
  let ttoeks = input[1].split(" ").map((t) => parseInt(t));

  let start = 0;
  let end = Math.max(...ttoeks);

  let min_size = 0;

  while (start <= end) {
    let mid = parseInt((start + end) / 2);
    let total = 0;

    for (let t of ttoeks) {
      // 떡이 자르고 오른쪽 걸 더한다.
      if (t > mid) {
        total += t - mid;
      }
    }

    // 실제로 자른게 더 적게 잘랐으면 더 작게 자른다.
    if (total < target) end = mid - 1;
    // 실제로 자른게 더 많이 잘랐으면 더 크게 자른다. (적어도 target만큼 얻었으니 일단 기록)
    else {
      start = mid + 1;
      min_size = mid;
    }
  }

  console.log(min_size);
});
