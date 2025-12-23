# https://leetcode.com/problems/gas-station/description/

def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    
    start = 0
    total = 0
    for i in range(len(gas)):
        if total + gas[i] < cost[i]:
            start = i + 1
            total = 0
        else:
            total += gas[i] - cost[i]
    
    return start
    
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(canCompleteCircuit(gas, cost))