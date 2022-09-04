const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input;

rl.on("line", (line) => {
  input = line;
});

rl.on("close", () => {
  let n = parseInt(input.split(" ")[0]);
  let k = parseInt(input.split(" ")[1]);

  let visited = new Array(100000).fill(1);

  const queue = [n];
  function bfs(x) {
    if (x === k) {
      console.log(result);
    }
    visited[x] = true;

    while (queue.length > 0) {
      loc = queue.shift();

      // -1 칸
      // +1 칸
      // *2 칸
    }
  }

  bfs(0, 0);
  console.log(map[n - 1][m - 1]);
  process.exit();
});
