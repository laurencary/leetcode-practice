from typing import List

def sortColors(nums: List[int]) -> None:
    i = 0 
    # print(len(nums))

    while i < len(nums):
        if nums[i] == 0:
            nums.insert(0, nums.pop(i))
        elif nums[i] == 2:
            nums.append(nums.pop(i))
        i += 1
        # print(nums)
        # break


nums = [2,0,2,1,1,0]
# sortColors(nums)
# print(nums)


def uncompress(s):
    res = ''
    start_num = 0

    while start_num < len(s):
        
        end_num = start_num

        while s[end_num + 1].isdigit():
            end_num += 1
        res += s[end_num + 1] * int(s[start_num:end_num + 1])
        start_num = end_num + 2
    return res


# print(uncompress("2c3a1t"))


from collections import defaultdict

def anagrams(s1, s2):
    c1 = {}
    c2 = {}
    
    for i in range(len(s1)):
        if s1[i] not in c1: c1[s1[i]] = 0
        c1[s1[i]] += 1
        
    for i in range(len(s2)):
        if s2[i] not in c2: c2[s2[i]] = 0
        c2[s2[i]] += 1

    return c1 == c2

# print(anagrams('restful', 'fluster'))


def pair_sum(numbers, target_sum):
    hash = {}
    i = 0
    while i < len(numbers):
        if numbers[i] in hash:
            return (hash[numbers[i]], i)
        else:
            hash[target_sum - numbers[i]] = i
        i += 1

# print(pair_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2))

def five_sort(nums):
    i = 0
    j = len(nums) - 1
    
    while i < j:
        while nums[j] == 5:
            j -= 1
        
        if nums[i] == 5:
            
            nums[i], nums[j] = nums[j],nums[i]
        
        i += 1
        j -= 1
    
    return nums

# print(five_sort([5, 5, 6, 5, 5, 5, 5]))

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

def reverse_list(head):
  curr = head
  prev = None
  
  while curr is not None:
    print(curr.value)
    next = curr.next
    curr.next = prev
    curr = next
    prev = curr
  return prev

print(reverse_list(a)) # f -> e -> d -> c -> b -> a