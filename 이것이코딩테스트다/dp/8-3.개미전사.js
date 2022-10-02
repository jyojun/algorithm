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
  let store = input[1].split(" ").map((s) => parseInt(s));
  let dp = new Array(n).fill(0);

  dp[0] = store[0];
  dp[1] = store[1];

  for (let i = 2; i < n; i++) {
    dp[i] = Math.max(store[i] + dp[i - 2], dp[i - 1]);
  }

  console.log(dp[n - 1]);
});
