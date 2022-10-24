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
  let screen = input.slice(1).map((v) => v.split("").map((vv) => parseInt(vv)));

  let result = "";
  function recursion(n, x, y) {
    const num = screen[x][y];
    let numCount = 0;
    for (let i = 0; i < n; i++)
      for (let j = 0; j < n; j++) {
        if (screen[x + i][y + j] === num) numCount++;
        else break;
      }

    if (numCount === n * n) result += String(num);
    else {
      result += "(";
      n /= 2;
      for (let i = 0; i < 2; i++)
        for (let j = 0; j < 2; j++) recursion(n, x + i * n, y + j * n);
      result += ")";
    }
  }

  recursion(n, 0, 0);
  console.log(result);
});
