class MaxHeap {
    constructor() {
        this.array = [null];
    }

    getParent(idx) {
        return Math.floor(idx / 2);
    }

    getLeftChild(idx) {
        return idx * 2;
    }

    getRightChild(idx) {
        return idx * 2 + 1;
    }

    siftUp(idx) {
        if (idx === 1) return;

        let parentIdx = this.getParent(idx);
        if (this.array[idx] > this.array[parentIdx]) {
            [this.array[idx], this.array[parentIdx]] = [this.array[parentIdx], this.array[idx]]
            this.siftUp(parentIdx);
        }
    }

    insert(val) {
        this.array.push(val);
        this.siftUp(this.array.length - 1);
    }

    siftDown(idx) {
        if (idx === this.array.length - 1) return;
        
        const leftChildIdx = this.getLeftChild(idx);
        const rightChildIdx = this.getRightChild(idx);

        const leftChild = this.array[leftChildIdx] === undefined ? -Infinity : this.array[leftChildIdx]
        const rightChild = this.array[rightChildIdx] === undefined ? -Infinity : this.array[rightChildIdx]

        if (this.array[idx] > leftChild && this.array[idx] > rightChild) return;

        let swapIdx;
        if (rightChild < leftChild) {
            swapIdx = leftChildIdx;
        } else {
            swapIdx = rightChildIdx;
        }

        [this.array[idx], this.array[swapIdx]] = [ this.array[swapIdx], this.array[idx]]
        this.siftDown(swapIdx);
    }

    deleteMax() {
        if (this.array.length === 1) return null;
        if (this.array.length === 2) return this.array.pop();
        
        const max = this.array[1];
        this.array[1] = this.array.pop();
        this.siftDown(1);

        return max;
    }
}

module.exports = {
    MaxHeap
};