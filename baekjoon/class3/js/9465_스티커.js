let input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    let t = parseInt(input.shift());
    for (let i = 0; i < t; i++) {
      let n = parseInt(input.shift());
      let stickers = Array.from({ length: n + 1 }, () => new Array(2).fill(0));
      input
        .shift()
        .split(" ")
        .map((v, idx) => (stickers[idx + 1][0] = Number(v)));
      input
        .shift()
        .split(" ")
        .map((v, idx) => (stickers[idx + 1][1] = Number(v)));

      for (let j = 1; j <= n; j++) {
        if (j < 3) {
          stickers[j][0] += stickers[j - 1][1];
          stickers[j][1] += stickers[j - 1][0];
        } else {
          stickers[j][0] += Math.max(
            stickers[j - 1][1],
            Math.max(...stickers[j - 2])
          );
          stickers[j][1] += Math.max(
            stickers[j - 1][0],
            Math.max(...stickers[j - 2])
          );
        }
      }

      console.log(Math.max(...stickers[n]));
    }
  });
