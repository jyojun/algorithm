const input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", function (line) {
    input.push(line);
  })
  .on("close", function () {
    let n = parseInt(input[0]);
    let map = input.slice(1).map((v) => v.split("").map((vv) => parseInt(vv)));
    let visited = Array.from(Array(n), () => Array(n).fill(false));
    let cnt = 0;
    let result = [];
    let dxdy = [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
    ];
    function dfs(x, y) {
      if (map[x][y] === 0) return;
      cnt++;
      visited[x][y] = true;
      dxdy.map((dxdy) => {
        let [dx, dy] = dxdy;
        let nx = x + dx;
        let ny = y + dy;
        if (nx >= 0 && ny >= 0 && nx < n && ny < n && !visited[nx][ny]) {
          dfs(nx, ny);
        }
      });
    }

    for (let i = 0; i < n; i++)
      for (let j = 0; j < n; j++) {
        if (!visited[i][j]) {
          dfs(i, j);
          if (cnt > 0) {
            result.push(cnt);
            cnt = 0;
          }
        }
      }
    console.log(result.length);
    result.sort((a, b) => a - b);
    result.map((x) => console.log(x));
  });
