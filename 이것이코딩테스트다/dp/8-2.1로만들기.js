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
  let x = parseInt(input[0].split(" ")[0]);
  let dp = new Array(30001).fill(0);

  for (let i = 2; i < x + 1; i++) {
    dp[i] = dp[i - 1] + 1;
    if (i % 5 === 0) dp[i] = Math.min(dp[i], dp[i / 5] + 1);
    if (i % 3 === 0) dp[i] = Math.min(dp[i], dp[i / 3] + 1);
    if (i % 2 === 0) dp[i] = Math.min(dp[i], dp[i / 2] + 1);
  }

  console.log(dp[x]);
});
