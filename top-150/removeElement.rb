require ('byebug')

# @param {Integer[]} nums
# @param {Integer} val
# @return {Integer}
def remove_element(nums, val)
    nums.select! { |n| n != val }
    return nums.length
end

nums = [3,2,2,3]
p remove_element(nums, 3)
p nums