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

function solution(input) {
  let h = parseInt(input);
  let cnt = 0;
  for (let i = 0; i <= h; i++)
    for (let j = 0; j < 60; j++)
      for (let k = 0; k < 60; k++) {
        let time = String(i) + String(j) + String(k);
        if (time.includes("3")) cnt++;
      }

  console.log(cnt);
}
