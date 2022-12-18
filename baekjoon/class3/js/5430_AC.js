let input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    let t = parseInt(input.shift());
    let answer = "";

    for (let i = 0; i < t; i++) {
      let order = input.shift().split("");
      let num = parseInt(input.shift());
      let nums = input.shift();
      let isReverse = false;
      let flag = true;

      nums = nums.replaceAll("[", "");
      nums = nums.replaceAll("]", "");
      if (nums) nums = nums.split(",").map((v) => parseInt(v));
      else nums = [];

      for (j of order) {
        if (j === "R") isReverse = !isReverse;
        else if (j === "D") {
          if (nums.length <= 0) {
            answer += "error\n";
            flag = !flag;
            break;
          }
          if (isReverse) nums.pop();
          else nums.shift();
        }
      }
      if (isReverse) nums.reverse();
      if (flag) answer += "[" + nums.join(",") + "]" + "\n";
    }

    console.log(answer);
  });
