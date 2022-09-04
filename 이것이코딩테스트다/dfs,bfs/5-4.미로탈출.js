const readline = require("readline");
const { getMaxListeners } = require("process");

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
  let map = input
    .slice(1)
    .map((col) => col.split("").map((row) => parseInt(row)));

  const dx = [1, 0, -1, 0];
  const dy = [0, 1, 0, -1];

  let visited = new Array();
  for (let i = 0; i < n; i++) visited.push(Array(m).fill(false));

  function bfs(x, y) {
    const queue = [[x, y]];
    visited[x][y] = true;

    while (queue.length > 0) {
      loc = queue.shift();
      for (let i = 0; i < 4; i++) {
        let nx = loc[0] + dx[i];
        let ny = loc[1] + dy[i];
        if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
          if (map[nx][ny] === 1 && !visited[nx][ny]) {
            map[nx][ny] += map[loc[0]][loc[1]];
            queue.push([nx, ny]);
          }
        }
      }
    }
  }

  bfs(0, 0);
  console.log(map[n - 1][m - 1]);
  process.exit();
});
