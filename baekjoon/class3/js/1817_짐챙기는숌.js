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
  const [n, m] = input.shift().split(" ").map(Number);
  if (n === 0) {
    console.log(0);
    return;
  }
  const weights = input.shift().split(" ").map(Number);
  let curr_weight = 0;
  let cnt = 1;
  for (let w of weights) {
    curr_weight += w;
    if (curr_weight > m) {
      cnt += 1;
      curr_weight = w;
    }
  }
  console.log(cnt);
});
