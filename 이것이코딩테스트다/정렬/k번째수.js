function solution(array, commands) {
  const answer = [];

  commands.map((v) =>
    answer.push(
      array.slice(v[0] - 1, v[1]).sort(function (a, b) {
        return a - b;
      })[v[2] - 1]
    )
  );

  return answer;
}

function solution(numbers) {
  var answer = numbers
    .map((v) => v + "")
    .sort((a, b) => (b + a) * 1 - (a + b) * 1)
    .join("");

  return answer[0] === "0" ? "0" : answer;
}
