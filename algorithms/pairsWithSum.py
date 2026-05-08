# Time Complexity: O(N * M + R log R) where N, M are array lengths, R is result pairs count
# Space Complexity: O(M) for frequency map of arr2
#
# https://www.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x5808/1

def allPairs(target, arr1, arr2):
    from collections import Counter

    freq = Counter(arr2)
    result = []

    for u in arr1:
        v = target - u
        if v in freq:
            for _ in range(freq[v]):
                result.append((u, v))

    result.sort()
    return result
                
                