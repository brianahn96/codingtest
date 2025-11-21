# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

def searchRange(nums: list[int], target: int) -> list[int]:
    
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
    
    return [binary(nums, target, True), binary(nums, target, False)]

