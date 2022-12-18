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
  const word = input.shift().split("");
  let ans = "";
  for (let i = 0; i < word.length; i++) ans += i + "\n";
  console.log(ans);
});
