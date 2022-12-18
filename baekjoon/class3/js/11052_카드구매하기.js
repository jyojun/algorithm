let input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    const n = parseInt(input.shift());
    const p = [0];
    input
      .shift()
      .split(" ")
      .map((v) => p.push(Number(v)));
    const dp = new Array(n + 1).fill(0);
    dp[1] = p[1];

    for (let i = 1; i <= n; i++) {
      for (let j = 1; j <= i; j++) {
        dp[i] = Math.max(dp[i], dp[i - j] + dp[j], p[i]);
      }
    }

    console.log(dp[n]);
  });
