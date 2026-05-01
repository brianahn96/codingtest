# https://leetcode.com/problems/majority-element/description/

def majorityElement(nums: list[int]) -> int:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    
    half = len(nums) // 2
    first = majorityElement(nums[:half])
    last = majorityElement(nums[half:])
    
    if nums.count(first) > half:
        return first
    return last
    
nums = [2,2,1,1,1,2,2]
nums = [1,2,1,3,1,4,1,1]
print(majorityElement(nums))