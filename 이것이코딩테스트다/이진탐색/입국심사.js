function solution(n, times) {
  let answer = 0;

  let left = 0;
  let right = n * Math.max(...times);

  while (left <= right) {
    let mid = parseInt((left + right) / 2);
    let person = 0; // 한 심사관 당 심사할 수 있는 사람 수

    for (let time of times) person += parseInt(mid / time);
    if (person < n) {
      // 더 적게 심사할 수 있다면 시간을 늘린다.
      left = mid + 1;
    } else {
      // 더 많이 심사할 수 있다면 시간을 줄인다.
      answer = mid;
      right = mid - 1;
    }
  }
  return answer;
}
