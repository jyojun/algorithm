let input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    let [n, m] = input
      .shift()
      .split(" ")
      .map((v) => parseInt(v));
    let numerator = BigInt(1);
    let denominator = BigInt(1);

    for (let i = 1; i <= m; i++) {
      numerator *= BigInt(n--);
      denominator *= BigInt(i);
    }

    console.log((numerator / denominator).toString());
  });
