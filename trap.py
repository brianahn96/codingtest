# Given n non-negative integers representing an elevation map where the width of each bar is 1
# compute how much water it can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
# In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


from typing import List

def trapTwoPointer(height: List[int]) -> int:
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right += 1
        
    return volume

def trapStack(height: List[int]) -> int:
    stack = []
    volume = 0
    
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            
            if not len(stack):
                break
            
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            
            volume += distance * waters
        
        stack.append(i)
        
    return volume