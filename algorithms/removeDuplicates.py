
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicates(arr: list[int]) -> int:
    seen = set()
    
    idx = 0

    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            arr[idx] = arr[i]
            idx += 1
            
    return arr[:idx]