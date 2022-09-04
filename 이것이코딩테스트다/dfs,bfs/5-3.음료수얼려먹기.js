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
  let m = parseInt(input[0].split(" ")[1]);
  let mold = input
    .slice(1)
    .map((col) => col.split("").map((row) => parseInt(row)));

  function dfs(x, y) {
    if (x >= 0 && x < n && y >= 0 && y < m) {
      if (mold[x][y] === 0) {
        mold[x][y] = 1;
        dfs(x + 1, y);
        dfs(x, y + 1);
        dfs(x - 1, y);
        dfs(x, y - 1);

        return true;
      }
    }
    return false;
  }
  let cnt = 0;
  for (let i = 0; i < n; i++)
    for (let j = 0; j < m; j++) {
      if (dfs(i, j) === true) cnt++;
    }

  console.log(cnt);
  process.exit();
});
