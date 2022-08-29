const fs = require("fs");
let input = fs.readFileSync("./stdin/4-4").toString().split("\n");

let size = input[0].split(" ").map((d) => parseInt(d));
let user = input[1].split(" ").map((d) => parseInt(d));
let map = input
  .slice(2)
  .map((row) => row.split(" ").map((col) => parseInt(col)));
let dx = [-1, 0, 1, 0];
let dy = [0, 1, 0, -1];
let cnt = 1;

function turn() {
  let currLoc = [user[0], user[1]];
  let currDir = user[2];

  for (let i = 0; i < 4; i++) {
    currDir--;
    if (currDir < 0) {
      currDir = 3;
    }

    if (map[currLoc[0] + dx[currDir]][currLoc[1] + dy[currDir]] === 0)
      return currDir;
  }

  return -1;
}

function move() {
  let nextDir = turn();

  while (nextDir > 0) {
    map[user[0] + dx[nextDir]][user[1] + dy[nextDir]] = 1;
    user = [user[0] + dx[nextDir], user[1] + dy[nextDir], nextDir];
    cnt++;
    nextDir = turn();
  }
}

function solution() {
  // 처음 있는 곳 방문
  map[user[0]][user[1]] = 1;
  move(user, map);
  console.log(cnt);
}

solution();
