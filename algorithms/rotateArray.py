def rotate1(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    res = [0] * len(nums)
    
    for i in range(len(nums)):
        res[(i + k) % len(nums)] = nums[i]
    
    for i in range(len(nums)):
        nums[i] = res[i]
    
def rotate2(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)

    nums.reverse()
    
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    

def rotate3(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k]

nums = [1,2,3,4,5,6,7]
k = 3

rotate2(nums, k)
print(nums)