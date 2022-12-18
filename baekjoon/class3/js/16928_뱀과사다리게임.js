let input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    let [n, m] = input.shift().split(" ").map(Number);
    let snakes = new Array(101).fill(0);
    input.map((v) => {
      let [a, b] = v.split(" ").map(Number);
      snakes[a] = b;
    });

    let queue = [[1, 0]];
    let dice = [1, 2, 3, 4, 5, 6];
    let visited = new Array(101).fill(false);
    let min_tries = 101;
    visited[1] = true;
    const bfs = () => {
      while (queue.length > 0) {
        let [curr_loc, tries] = queue.shift();

        if (curr_loc === 100) {
          return tries;
        }

        for (d of dice) {
          let next_loc = curr_loc + d;
          if (!visited[next_loc] && next_loc > 0 && next_loc <= 100) {
            if (snakes[next_loc] === 0) {
              visited[next_loc] = true;
              queue.push([next_loc, tries + 1]);
            } else {
              if (!visited[snakes[next_loc]]) {
                visited[snakes[next_loc]] = true;
                queue.push([snakes[next_loc], tries + 1]);
              }
            }
          }
        }
      }
    };

    console.log(bfs());
  });
