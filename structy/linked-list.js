/*
Write a function, zipperLists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.
*/

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}


const zipperLists = (head1, head2) => {
    let curr = head1;
    let next = head2;

    while (next !== null) {
        console.log(curr.val)
        console.log(next.val)
        let temp = curr.next;
        curr.next = next;

        curr = next;
        next = temp;
    }

    return head1;
}


// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// a.next = b;
// b.next = c;
// // a -> b -> c

// const x = new Node("x");
// const y = new Node("y");
// const z = new Node("z");
// x.next = y;
// y.next = z;
// // x -> y -> z

// let result = zipperLists(a, x);
// // a -> x -> b -> y -> c -> z

// while (result !== null) {
//     console.log(result.val)
//     result = result.next
// }

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");
a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;
// a -> b -> c -> d -> e -> f

const x = new Node("x");
const y = new Node("y");
const z = new Node("z");
x.next = y;
y.next = z;
// x -> y -> z

zipperLists(a, x);
// a -> x -> b -> y -> c -> z -> d -> e -> f

// zipperLists(a, x);
// let result = zipperLists(a, x);

// while (result !== null) {
//     console.log(result.val)
//     result = result.next
// }



// const s = new Node("s");
// const t = new Node("t");
// s.next = t;
// // s -> t

// const one = new Node(1);
// const two = new Node(2);
// const three = new Node(3);
// const four = new Node(4);
// one.next = two;
// two.next = three;
// three.next = four;
// // 1 -> 2 -> 3 -> 4

// zipperLists(s, one);
// s -> 1 -> t -> 2 -> 3 -> 4