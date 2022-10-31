let input = [];
require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    let n = parseInt(input[0]);
    let matrix = input
      .slice(1)
      .map((v) => v.split(" ").map((vv) => parseInt(vv)));

    matrix.map((v, i) =>
      v.map((vv, j) => {
        if (vv === 0) matrix[i][j] = 101;
      })
    );
    let graph = Array.from(Array(n), () => Array(n).fill(0));

    for (let k = 0; k < n; k++) {
      for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
          matrix[i][j] = Math.min(matrix[i][j], matrix[i][k] + matrix[k][j]);
        }
      }
    }

    matrix.map((v, i) =>
      v.map((vv, j) => {
        if (vv === 101) graph[i][j] = 0;
        else graph[i][j] = 1;
      })
    );

    graph.map((v) => console.log(v.join(" ")));
  });
