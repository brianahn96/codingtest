# https://leetcode.com/problems/combination-sum-ii/

def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    result = []

    def dfs(cumul, index, path):

        if cumul < 0:
            return

        if cumul == 0:
            result.append(path)
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            dfs(cumul - candidates[i], i + 1, path + [candidates[i]])

    candidates.sort()
    dfs(target, 0, [])
    return result