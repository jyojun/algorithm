// 백준 5585번 거스름돈

function solution(price) {
  const coins = [500, 100, 50, 10, 5, 1];

  let change = 1000 - price;
  let cnt = 0;
  for (const c of coins) {
    cnt += parseInt(change / c);
    change = change % c;
  }
  console.log(cnt);
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input;
rl.on("line", (line) => {
  input = line;
  rl.close();
}).on("close", () => {
  solution(input);
  process.exit();
});
