let input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    const t = parseInt(input.shift());
    for (let i = 0; i < t; i++) {
      let tree = input.shift().split("");
      let depth = 0;
      let maxDepth = 0;
      for (let j = 0; j < tree.length; j++) {
        if (tree[j] === "[") depth += 1;
        else depth -= 1;

        if (depth > maxDepth) maxDepth = depth;
      }

      console.log(2 ** maxDepth);
    }
  });
