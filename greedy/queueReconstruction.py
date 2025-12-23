# https://leetcode.com/problems/queue-reconstruction-by-height/description/

import heapq

def reconstructQueue(people: list[list[int]]) -> list[list[int]]:
    queue = []
    
    for person in people:
        heapq.heappush(queue, (-person[0], person[1]))
    
    # print(queue)
    results = []
    while queue:
        person = heapq.heappop(queue)
        results.insert(person[1], [-person[0],person[1]])
    return results

people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]

print(reconstructQueue(people))