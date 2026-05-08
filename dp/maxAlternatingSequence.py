# https://leetcode.com/problems/maximum-alternating-subsequence-sum/description/

def maxAlternatingSumDP(nums: list[int]) -> int:
    memo = {}

    def solve(i, is_even):
        if i == len(nums):
            return 0
        if (i, is_even) in memo:
            return memo[(i, is_even)]

        # 1. 현재 숫자를 건너뛰는 경우
        skip = solve(i + 1, is_even)
        
        # 2. 현재 숫자를 포함하는 경우
        val = nums[i] if is_even else -nums[i]
        include = val + solve(i + 1, not is_even)
        
        memo[(i, is_even)] = max(skip, include)
        return memo[(i, is_even)]

    return solve(0, True)

def maxAlternatingSum(nums: list[int]) -> int:
    even_sum = 0
    odd_sum = 0
    
    for num in nums:
        # 현재 숫자를 더해서 짝수 인덱스로 끝내는 경우
        # (이전까지 홀수 인덱스로 끝난 합에 현재 값을 더함)
        new_even = max(even_sum, odd_sum + num)
        
        # 현재 숫자를 빼서 홀수 인덱스로 끝내는 경우
        # (이전까지 짝수 인덱스로 끝난 합에서 현재 값을 뺌)
        new_odd = max(odd_sum, even_sum - num)
            
        even_sum, odd_sum = new_even, new_odd
            
    # 결과적으로 숫자를 더해서 끝내는 것이 항상 이득이므로 even_sum 반환
    return even_sum