// ============================================================================
// Implementation Exercise: Singly Linked List
// ============================================================================
//
// -------
// Prompt:
// -------
//
// Implement a Singly Linked List and all of its methods below!
//
// ------------
// Constraints:
// ------------
//
// Make sure the time and space complexity of each is equivalent to those 
// in the table provided in the Time and Space Complexity Analysis section
// of your Linked List reading!
//
// -----------
// Let's Code!
// -----------

// TODO: Implement a Linked List Node class here
class Node {
    constructor(val) {
        this.value = val
        this.next = null
    }

}

// TODO: Implement a Singly Linked List class here
class LinkedList {
    constructor() {
        this.head = null
        this.tail = null
        this.length = 0
    }

    // TODO: Implement the addToTail method here
    addToTail(val) {
        const newNode = new Node(val)
        if (this.length > 0) {
            this.tail.next = newNode
        } else {
            this.head = newNode
        }        

        this.tail = newNode
        this.length += 1

        return this
    }

    // TODO: Implement the removeTail method here
    removeTail() {
        if (this.length === 0) return undefined

        const oldTail = this.tail

        if (this.length === 1) {
            this.head = null
            this.tail = null
        } else {
            const newTail = this.get(this.length - 2)
            newTail.next = null
            this.tail = newTail
        }
        this.length -= 1
        return oldTail
    }

    // TODO: Implement the addToHead method here
    addToHead(val) {
        const newHead = new Node(val)
        newHead.next = this.head
        this.head = newHead
        this.length += 1

        if (this.length === 1) this.tail = newHead

        return this
    }

    // TODO: Implement the removeHead method here
    removeHead() {
        if (this.length === 0) return undefined
        const oldHead = this.head
        
        if (this.length === 1) {
            this.head = null
            this.tail = null
        } else {
            const newHead = this.head.next
            this.head = newHead
        }


        this.length -= 1
        return oldHead;
    }

    // TODO: Implement the contains method here
    contains(target) {
        let curr = this.head

        while (curr) {
            if (curr.value === target) return true
            curr = curr.next
        }

        return false
    }

    // TODO: Implement the get method here
    get(index) {
        if (index >= this.length) return null

        let curr = this.head
        for (let i = 1; i <= index; i++) {
            curr = curr.next
        }

        return curr
    }

    // TODO: Implement the set method here
    set(index, val) {
        if (index >= this.length) return false 
        const prev = this.get(index - 1);
        if (prev) {
            const newNode = new Node(val)
            const newNext = prev.next.next
            prev.next = newNode
            newNode.next = newNext

            return true
        }

        return false
    }

    // TODO: Implement the insert method here
    insert(index, val) {
        if (index >= this.length) return false
        const prev = this.get(index - 1);
        if (prev) {
            const newNode = new Node(val)
            const newNext = prev.next
            prev.next = newNode
            newNode.next = newNext

            this.length += 1
            return true
        }

        return false
    }

    // TODO: Implement the remove method here
    remove(index) {
        if (this.length === 0 || index >= this.length) return undefined

        const prev = this.get(index - 1);

        const oldNode = prev.next
        prev.next = oldNode.next     

        this.length -= 1
        return oldNode
    }

    // TODO: Implement the size method here
    size() {
        return this.length
    }
}

exports.Node = Node;
exports.LinkedList = LinkedList;
