function solution(numbers) {
  var answer = "";
  numbers = numbers
    .map((n) => String(n))
    .sort(function (a, b) {
      return b.repeat(4).substr(0, 4) - a.repeat(4).substr(0, 4);
    })
    .map((n) => (answer += n));
  return answer[0] === "0" ? "0" : answer;
}
