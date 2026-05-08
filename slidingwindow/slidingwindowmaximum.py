# https://leetcode.com/problems/sliding-window-maximum/description/

from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
        output = []
        q = deque()
        
        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            
            q.append(i)
            
            if q[0] < i - k + 1:
                q.popleft()
            
            if i >= k - 1:
                output.append(nums[q[0]])
                
        return output

nums = [1,3,-1,-3,5,3,6,7]
k = 3

# nums = [1,3,1,2,0,5]
# k = 3

print(maxSlidingWindow(nums, k))