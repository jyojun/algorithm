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

  let graph = Array.from(Array(n + 1), () => Array(n + 1).fill(101));

  for (let i = 1; i < m + 1; i++) {
    let a = parseInt(input[i].split(" ")[0]);
    let b = parseInt(input[i].split(" ")[1]);
    graph[a][a] = 0;
    graph[b][b] = 0;
    graph[a][b] = 1;
    graph[b][a] = 1;
  }

  for (let k = 1; k < n + 1; k++)
    for (let i = 1; i < n + 1; i++)
      for (let j = 1; j < n + 1; j++)
        graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);

  let minIdx;
  let minValue = 505;
  for (let i = 1; i < n + 1; i++) {
    const result =
      graph[i].reduce(function add(sum, currValue) {
        return sum + currValue;
      }, 0) - 101;

    if (result < minValue) {
      minValue = result;
      minIdx = i;
    }
  }
  console.log(minIdx);
});
