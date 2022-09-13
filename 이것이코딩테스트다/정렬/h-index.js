function solution(citations) {
  citations = citations.sort((a, b) => b - a);
  let i = 0;

  while (citations[i] > i) i += 1;
  return i;
}
