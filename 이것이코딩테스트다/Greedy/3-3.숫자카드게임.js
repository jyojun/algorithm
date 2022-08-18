const fs = require("fs");
let input = fs.readFileSync("./stdin/3-3").toString().split("\n");

function solution(input) {
  let n, m;
  let info = input[0].split(" ").map((d) => parseInt(d));
  let cards = input.slice(1).map((c) => c.split(" ").map((d) => parseInt(d)));
  n = info[0];
  m = info[1];

  let result = new Array();
  for (const row of cards) {
    result.push(Math.min(...row));
  }
  console.log(Math.max(...result));
}

solution(input);
