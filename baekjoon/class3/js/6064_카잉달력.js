let input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", function (line) {
    input.push(line);
  })
  .on("close", function () {
    let t = parseInt(input[0]);
    let result = [];

    for (let i = 0; i < t; i++) {
      let n = parseInt(input[i + 1].split(" ")[0]);
      let m = parseInt(input[i + 1].split(" ")[1]);
      let x = parseInt(input[i + 1].split(" ")[2]);
      let y = parseInt(input[i + 1].split(" ")[3]);
      let cnt = 0;

      // 정답을 k로 가정했을 때, k값은 x값을 뺐을 때와, y값을 뺐을 때 둘다 각각 n, m 의 나머지가 0이 됨을 이용
      for (let k = x; k <= icm(n, m); k += n) {
        // 최소공배수로 연산을 줄임
        if ((k - y) % m === 0) {
          result.push(k);
          cnt++;
        }
      }
      if (!cnt) {
        result.push(-1);
      }
    }
    result.map((v) => console.log(v));
  });

function gcd(a, b) {
  while (b !== 0) {
    let r = a % b;
    a = b;
    b = r;
  }
  return a;
}

function icm(a, b) {
  return (a * b) / gcd(a, b);
}
