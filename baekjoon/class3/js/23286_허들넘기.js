let input = [];
require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    let [n, m, t] = input.shift().split(" ").map(Number);
    let graph = Array.from({ length: n + 1 }, () =>
      Array.from({ length: n + 1 }, () => Infinity)
    );
    let ans = Array.from({ length: n + 1 }, () =>
      Array.from({ length: n + 1 }, () => Infinity)
    );
    for (let i = 1; i <= n; i++) ans[i][i] = 0;
    input.slice(0, m).map((v) => {
      let [a, b, h] = v.split(" ").map(Number);
      graph[a][b] = h;
      ans[a][b] = h;
    });

    for (let k = 1; k <= n; k++) {
      for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= n; j++) {
          ans[i][j] = Math.min(ans[i][j], Math.max(ans[i][k], ans[k][j]));
        }
      }
    }
    input.slice(m).forEach((v) => {
      let [a, b] = v.split(" ").map(Number);
      let temp = ans[a][b];
      if (temp === Infinity) console.log(-1);
      else console.log(temp);
    });
  });
