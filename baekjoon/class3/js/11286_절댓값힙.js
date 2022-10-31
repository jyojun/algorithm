let input = [];

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", function (line) {
    input.push(line);
  })
  .on("close", function () {
    let n = parseInt(input[0]);
    let order = input.slice(1).map((v) => parseInt(v));

    let heap = new Heap();

    order.map((v) => {
      if (v === 0 && heap.heap.length === 0) console.log(0);
      else if (v === 0 && heap.heap.length !== 0) {
        console.log(heap.remove());
      } else {
        heap.insert(v);
      }
    });
  });

/* min heap 
왼쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2 + 1
오른쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2 + 2
부모 노드 인덱스 = (자식 노드 인덱스 - 1) / 2
*/

class Heap {
  constructor() {
    this.heap = [];
  }

  getLeftChildIndex = (parentIndex) => parentIndex * 2 + 1;
  getRightChildIndex = (parentIndex) => parentIndex * 2 + 2;
  getParentIndex = (childIndex) => parseInt((childIndex - 1) / 2);

  peek = () => this.heap[0];

  insert = (value) => {
    this.heap.push(value);
    this.heapifyUp();
  };

  heapifyUp = () => {
    let index = this.heap.length - 1; // 계속해서 변하는 index 값
    const lastInsertedValue = this.heap[index];

    // 루트 노드까지 올라갈 때 까지
    while (index > 0) {
      let parentIndex = this.getParentIndex(index);
      let parent = this.heap[parentIndex];

      // 부모 노드의 값이 마지막에 삽입한 값보다 크다면
      // 부모의 자리를 계속해서 아래로 내린다.

      if (
        Math.abs(this.heap[index]) > Math.abs(this.heap[parentIndex]) ||
        (Math.abs(this.heap[index]) === Math.abs(this.heap[parentIndex]) &&
          this.heap[index] > this.heap[parentIndex])
      )
        break;

      this.heap[parentIndex] = lastInsertedValue;
      this.heap[index] = parent;
      index = parentIndex;
    }
  };

  remove = () => {
    const root = this.heap[0];
    const end = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = end;
      this.heapifyDown();
    }
    return root;
  };

  heapifyDown = () => {
    let index = 0; // 루트 인덱스
    const count = this.heap.length;
    const root = this.heap[index];

    // 계속해서 left child 가 있을 때 까지 검사. (left가 없으면 right도 없기 때문)
    while (true) {
      let leftChildIndex = this.getLeftChildIndex(index);
      let rightChildIndex = this.getRightChildIndex(index);

      // 왼쪽, 오른쪽 중에 더 작은 값을 찾는다.
      // rightChild가 있다면 비교해서 더 작은 값을 찾는다.
      // 없다면 leftChild가 더 작은 값을 가진 인덱스가 된다.
      let smallerChildIndex = null;

      if (leftChildIndex < count) {
        if (
          Math.abs(this.heap[leftChildIndex]) < Math.abs(this.heap[index]) ||
          (Math.abs(this.heap[leftChildIndex]) === Math.abs(this.heap[index]) &&
            this.heap[leftChildIndex] < this.heap[index])
        ) {
          smallerChildIndex = leftChildIndex;
        }
      }

      if (rightChildIndex < count) {
        if (smallerChildIndex === null) {
          if (
            Math.abs(this.heap[rightChildIndex]) < Math.abs(this.heap[index]) ||
            (Math.abs(this.heap[rightChildIndex]) ===
              Math.abs(this.heap[index]) &&
              this.heap[rightChildIndex] < this.heap[index])
          ) {
            smallerChildIndex = rightChildIndex;
          }
        } else {
          if (
            Math.abs(this.heap[rightChildIndex]) <
              Math.abs(this.heap[leftChildIndex]) ||
            (Math.abs(this.heap[rightChildIndex]) ===
              Math.abs(this.heap[leftChildIndex]) &&
              this.heap[rightChildIndex] < this.heap[leftChildIndex])
          ) {
            smallerChildIndex = rightChildIndex;
          }
        }
      }

      if (smallerChildIndex === null) break;

      // 자식 값이 루트 값보다 작다면 위로 끌어올린다.

      this.heap[index] = this.heap[smallerChildIndex];
      this.heap[smallerChildIndex] = root;
    }
  };
}
