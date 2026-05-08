# Time Complexity: O(log n) for binary search variants
# Space Complexity: O(1) - Only using constant extra space
#
# https://leetcode.com/problems/binary-search/description/

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 
# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

def lower_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


def binary(nums, target, findFirst):
    s, e = 0, len(nums) - 1
    ans = -1
    while s <= e:
        mid = (s + e) // 2
        if target > nums[mid]:
            s = mid + 1
        elif target < nums[mid]:
            e = mid - 1
        else:
            ans = mid
            if findFirst:
                e = mid - 1
            else:
                s = mid + 1
    return ans
arr = [1, 2, 2, 2, 4, 5]
# arr = [1, 2]
target = 3
print(lower_bound(arr, target))
print(upper_bound(arr, target))
# print(binary(arr, target, True))
# print(binary(arr, target, False))
# print(search(arr, target))