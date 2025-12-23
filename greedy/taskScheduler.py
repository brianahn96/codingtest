# https://leetcode.com/problems/task-scheduler/description/

from collections import Counter

def leastInterval(tasks: list[str], n: int) -> int:
    counter = Counter(tasks)
    result = 0
    
    while True:
        sub_count = 0
        
        for task, _ in counter.most_common(n + 1):
            sub_count += 1
            result += 1
            
            counter.subtract(task)
            counter += Counter()
        
        if not counter:
            break
        
        result += n - sub_count + 1
    
    return result

tasks = ["A","C","A","B","D","B"]
n = 1

tasks = ["A","A","A","B","B","B"]
n = 2

print(leastInterval(tasks, n))