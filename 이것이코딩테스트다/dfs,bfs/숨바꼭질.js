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

  let visited = Array.from({ length: 100100 }, () => false);

  function bfs(x) {
    visited[x] = true;
    let queue = [[x, 0]];
    while (queue.length > 0) {
      let loc = queue.shift();
      let dx;

      if (loc[0] === k) {
        console.log(loc[1]);
        return;
      }

      // -1 칸
      dx = loc[0] - 1;
      if (0 <= dx && dx <= 100000 && visited[dx] === false) {
        visited[dx] = true;
        queue.push([dx, loc[1] + 1]);
      }
      // +1 칸
      dx = loc[0] + 1;
      if (0 <= dx && dx <= 100000 && visited[dx] === false) {
        visited[dx] = true;
        queue.push([dx, loc[1] + 1]);
      }
      // *2 칸
      dx = loc[0] * 2;
      if (0 <= dx && dx <= 1000000 && visited[dx] === false) {
        visited[dx] = true;
        queue.push([dx, loc[1] + 1]);
      }
    }
  }

  bfs(n);
});
