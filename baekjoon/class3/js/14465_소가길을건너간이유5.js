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
  const [n, k, b] = input.shift().split(" ").map(Number);

  const isNormal = new Array(n + 1).fill(true);

  for (let i = 0; i < b; i++) isNormal[parseInt(input.shift())] = false;
  let ans = 0;
  for (let i = 1; i <= k; i++) if (isNormal[i]) ans += 1;
  let prefix_sum = [ans];
  for (let i = k + 1; i <= n; i++) {
    if (isNormal[i] && !isNormal[i - k]) ans += 1;
    else if (isNormal[i] && isNormal[i - k]) ans = ans;
    else if (!isNormal[i] && isNormal[i - k]) ans -= 1;
    else ans = ans;
    prefix_sum.push(ans);
  }

  console.log(k - Math.max(...prefix_sum));
});
