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
  let paper = input.slice(1).map((v) => v.split(" ").map((vv) => parseInt(vv)));

  let count = [0, 0, 0];
  function recursion(n, x, y) {
    const num = paper[x][y];
    let numCount = 0;
    for (let i = 0; i < n; i++)
      for (let j = 0; j < n; j++) {
        if (paper[x + i][y + j] === num) numCount++;
        else break;
      }

    if (numCount === n * n) count[num + 1]++;
    else {
      n /= 3;
      for (let i = 0; i < 3; i++)
        for (let j = 0; j < 3; j++) recursion(n, x + i * n, y + j * n);
    }
  }

  recursion(n, 0, 0);
  console.log(count.join("\n"));
});
