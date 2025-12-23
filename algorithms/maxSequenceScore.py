# https://leetcode.com/problems/maximum-subsequence-score/description/

import heapq

def maxScore(nums1: list[int], nums2: list[int], k: int) -> int:
    res, prefix, heap = 0, 0, []

    for first, last in sorted(list(zip(nums1, nums2)), key = lambda x: -x[-1]):
        prefix += first
        heapq.heappush(heap, first)
        if len(heap) == k:
            res = max(res, prefix * last)
            prefix -= heapq.heappop(heap)

    return res