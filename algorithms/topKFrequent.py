# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from typing import List
from collections import Counter
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    heap = []
    
    for num, freq in counter.items():
        heapq.heappush(heap, (-freq, num))

    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    return result