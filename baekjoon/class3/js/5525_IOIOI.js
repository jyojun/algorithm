let input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", function (line) {
    input.push(line);
  })
  .on("close", function () {
    let n = parseInt(input[0]);
    let m = parseInt(input[1]);
    let string = input[2];

    let result = [];
    let cnt = 0;
    let answer = 0;
    let i = 0;
    while (true) {
      if (i >= m - 2) break;
      if (string[i] === "I" && string[i + 1] === "O" && string[i + 2] === "I") {
        cnt++;
        i += 2;
      } else {
        if (cnt >= n) answer += cnt - n + 1;
        cnt = 0;
        i++;
      }
    }

    if (cnt >= n) {
      answer += cnt - n + 1;
    }
    console.log(answer);
  });
