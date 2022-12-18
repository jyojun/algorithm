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
  const n = parseInt(input.shift());
  let a = BigInt(1);
  let b = BigInt(1);
  let temp;
  const fibo = (n) => {
    if (n === 1 || n === 2) return BigInt(1);
    for (let i = 3; i <= n; i++) {
      temp = b;
      b = (a + b) % BigInt(1000000007);
      a = temp;
    }
    return b;
  };

  console.log(Number(fibo(n)), n - 2);
});
