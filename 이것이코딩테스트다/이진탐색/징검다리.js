function solution(distance, rocks, n) {
  let answer = 0;

  let left = 0;
  let right = distance;

  rocks.sort((a, b) => a - b);
  console.log(rocks);

  while (left <= right) {
    let mid = parseInt((left + right) / 2);
    let cnt = 0; // 제거 한 돌의 갯수 카운팅
    let curr_rock = 0;

    for (let i = 0; i < rocks.length; i++) {
      if (rocks[i] - curr_rock < mid) {
        // 이전 바위와의 거리 차이가 기준점보다 작다면, 제거
        cnt++;
      } else {
        // 그렇지 않다면 넘어간다.
        curr_rock = rocks[i];
      }
    }
    // console.log(mid, cnt)

    if (cnt > n) {
      // 실제보다 많이 제거했을 경우 너무 기준을 크게 잡다 기준을 작게 잡는다.
      right = mid - 1;
    } else {
      // 실제보다 적게 제거 했을 경우 너무 작게 잡아 기준을 크게 잡는다.
      answer = mid;
      left = mid + 1;
    }
  }
  return answer;
}
