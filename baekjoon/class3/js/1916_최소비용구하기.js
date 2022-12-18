let input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    let n = parseInt(input.shift());
    let m = parseInt(input.shift());
    let costs = Array.from({ length: n + 1 }, () =>
      new Array(n + 1).fill(Infinity)
    );

    input.slice(0, m).map((v) => {
      let [start, end, cost] = v.split(" ").map(Number);
      costs[start][end] = Math.min(costs[start][end], cost);
    });

    for (let i = 1; i <= n; i++) costs[i][i] = 0;

    let [start, dest] = input[m].split(" ").map(Number);

    let min_dist = new Array(n + 1).fill(Infinity);
    let visited = new Array(n + 1).fill(Infinity);
    for (let i = 1; i <= n; i++) min_dist[i] = costs[start][i];

    function get_smallest_node() {
      let min_distance = Infinity;
      let idx = 1;

      for (let i = 1; i <= n; i++) {
        if (min_dist[i] < min_distance && !visited[i]) {
          min_distance = min_dist[i];
          idx = i;
        }
      }
      return idx;
    }
    for (let i = 1; i <= n; i++) {
      let curr = get_smallest_node();
      visited[curr];
      for (let j = 1; j <= n; j++) {
        min_dist[curr] = Math.min(min_dist[curr], min_dist[curr] + costs[i]);
      }
    }

    console.log(min_dist[dest]);
  });
