let input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    let [s, t] = input[0].split(" ").map((v) => parseInt(v));
    let result = sum(t) - sum(s - 1);
    console.log(result);
  });

function sum(n) {
  let result = 0;
  for (let i = 1; i <= n; i++) {
    let temp = parseInt(n / i);
    result += temp * (-1) ** i;
  }
  return result;
}
