from typing import List

# valid parenthesis
def isValid(s: str) -> bool:
    if len(s) % 2 == 1: return False 

    parens = {"(":")","{":"}", "[":"]"}
    stack = []
    for p in s:
        if p in parens:
            stack.append(p)
        elif parens[stack[-1]] == p:
            stack.pop()
        else:
            return False
        # print(stack)
    
    return len(stack) == 0

# print(isValid("["))
# print(isValid("[]{}"))
# print(isValid("[]{(}"))

# merge-intervals

# will inputs always be sorted?
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    result = []
    for range in intervals:

        if result and range[0] <= result[-1][1]:
            result[-1][1] = max(range[1], result[-1][1])
        else:
            result.append(range)

    return result


test1 = [[8,10],[15,18],[1,3],[2,6]]
test2 = [[1,4],[4,5]]

# print(merge(test1)) #[[1,6],[8,10],[15,18]]
# print(merge(test2)) #[[1,5]]


#contains duplicates II

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:

    left = 0
    window = set()

    for right in range(len(nums)):
        if right - left > k:
            window.remove(nums[left])
            left += 1

        if nums[right] in window:
            return True
            
        window.add(nums[right])

    return False

# nums = [1,2,3,1]
# k = 3
# print(containsNearbyDuplicate(nums, k))

# nums = [1,0,1,1]
# k = 1
# print(containsNearbyDuplicate(nums, k))

# nums = [1,2,3,1,2,3]
# k = 2
# print(containsNearbyDuplicate(nums, k))

        
def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0

    window = set()
    left, right = 0, 0

    while right < len(s):
        while s[right] in window:
            window.discard(s[left])
            left += 1

        max_length = max(max_length, right - left + 1)
        window.add(s[right])
        right += 1

    return max(max_length, len(window))

# print(lengthOfLongestSubstring("au")) #3
# print(lengthOfLongestSubstring("bbbbb")) #1
# print(lengthOfLongestSubstring("pwwkew")) #3

def maxArea(height: List[int]) -> int:
    max_area = 0
    left = 0
    right = 1

    while right < len(height):
        max_area = max((right - left) * min(height[left], height[right]), max_area)
        if height[left] < height[right]:
            left += 1
        right += 1

    return max_area


# height = [1,8,6,2,5,4,8,3,7]
# print(maxArea(height)) #49


def minSubArrayLen(self, target: int, nums: List[int]) -> int:



target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))