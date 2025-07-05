# https://leetcode.com/problems/combination-sum/

from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:

    res = []
    
    def dfs(index, path):
        
        sums = sum(path)
        
        if sums == target:
            res.append(path)
            return
        
        if sums > target:
            return
        
        for i in range(index, len(candidates)):
            dfs(i, path + [candidates[i]])
    
    dfs(0, [])
    return res