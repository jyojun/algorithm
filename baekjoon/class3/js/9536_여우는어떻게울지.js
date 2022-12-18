let input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    let t = parseInt(input.shift());
    for (let i = 0; i < t; i++) {
      let cries = input.shift().split(" ");
      let fox = [];
      while (true) {
        let temp = input.shift();
        if (temp === "what does the fox say?") {
          break;
        }
        for (let j = 0; j < cries.length; j++) {
          if (cries[j] === temp.split(" ")[2]) cries[j] = "";
        }
      }
      for (let j of cries) if (j !== "") fox.push(j);
      console.log(fox.join(" "));
    }
  });
