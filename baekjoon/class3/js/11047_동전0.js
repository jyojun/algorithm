const input = [];
const strToNumArr = (str) =>
  str.split(" ").map((numString) => Number(numString));

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", function (line) {
    input.push(line.trim());
  })
  .on("close", function () {
      const [n, k] = strToNumArr(input.shift());
      const 
  });
