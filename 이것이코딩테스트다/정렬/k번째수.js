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


