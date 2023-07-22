class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_node(head, value, index):
    new_node = Node(value)
    prev = None
    next = head
    i = 0
    while i < index:
        print(i)
        print(next)
        prev = next
        next = head.next
        i += 1
        
    prev.next = new_node
    new_node.next = next
    
    return new_node if i == 0 else head

print(insert_node(a, 'x', 2))