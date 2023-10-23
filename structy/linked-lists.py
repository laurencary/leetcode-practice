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


# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# print(insert_node(a, 'x', 2))


def add_lists(head_1, head_2):
    carry = 0
    sum = Node(None)
    curr_1 = head_1
    curr_2 = head_2
    curr_sum = sum
    place = 1
    
    while curr_2 or curr_1:
        num_1 = curr_1.val if curr_1 else 0
        num_2 = curr_2.val if curr_2 else 0
        
        temp_sum = num_1 + num_2 + carry
        # print(num_1)
        # print(num_2)
        # print(temp_sum)
        if temp_sum > 9:
            carry = 1 
            temp_sum -= 10
        else:
            carry = 0
        
        new_node = Node(temp_sum)
        curr_sum.next = new_node
        curr_sum = new_node
        curr_1 = curr_1.next
        curr_2 = curr_2.next
        
    return sum.next


a1 = Node(1)
a2 = Node(2)
a3 = Node(6)
a1.next = a2
a2.next = a3
# 1 -> 2 -> 6

b1 = Node(4)
b2 = Node(5)
b3 = Node(3)
b1.next = b2
b2.next = b3
# 4 -> 5 -> 3

# print(add_lists(a1, b1).val)
# 5 -> 7 -> 9

[def seq_of_numbers(string):
    result = ''
    seq_count = 0
    curr_char = string[0]
    
    for char in string:
        if char == curr_char:
            seq_count += 1
        else:
            result += str(seq_count) + curr_char
            print(result)
            count = 1
            curr_char = char

    result += str(seq_count) + curr_char
            
    return result]

print(seq_of_numbers("1211"))