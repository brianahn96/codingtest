# https://leetcode.com/problems/partition-equal-subset-sum/description/

def canPartition(nums: list[int]) -> bool:
    target = sum(nums) // 2

    if sum(nums) % 2:
        return False

    dp = set()
    dp.add(0)
    for num in nums:
        nextdp = set()
        for t in dp:
            if (t + num) == target:
                return True
            nextdp.add(t + num)
            nextdp.add(t)
        dp = nextdp
    return False