def solution(readings):
    
    def reduce(reading):
        while reading >= 10:
            reading = sum([int(digit) for digit in str(reading)])
        return reading
    
    candidates = []
    for reading in readings:
        candidates.append(reduce(reading))
    from collections import Counter
    
    counter = Counter(candidates)

    max_value = max(counter.values())
    
    keys = [k for k, v in counter.items() if v == max_value]
    return max(keys)

# 테스트 예시
# print(solution([123, 456, 789, 101])) # 출력: 6

def solution2(matrix, commands):
    for cmd in commands:
        parts = cmd.split()
        action = parts[0]
        
        # 1. 행 바꾸기
        if action == "swapRows":
            r1, r2 = int(parts[1]), int(parts[2])
            matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
            
        # 2. 열 바꾸기
        elif action == "swapColumns":
            c1, c2 = int(parts[1]), int(parts[2])
            for i in range(len(matrix)):
                matrix[i][c1], matrix[i][c2] = matrix[i][c2], matrix[i][c1]
                
        # 3. 행 뒤집기
        elif action == "reverseRow":
            r = int(parts[1])
            matrix[r] = matrix[r][::-1]
            
        # 4. 열 뒤집기
        elif action == "reverseColumn":
            c = int(parts[1])
            # 해당 열의 값들만 뽑아서 뒤집은 뒤 다시 배치
            col_values = [matrix[i][c] for i in range(len(matrix))]
            col_values.reverse()
            for i in range(len(matrix)):
                matrix[i][c] = col_values[i]
                
        # 5. 시계방향 90도 회전
        elif action == "rotate90Clockwise":
            rows = len(matrix)
            cols = len(matrix[0])
            
            # 1. 새로운 크기(cols x rows)의 빈 행렬 생성
            # 행과 열의 개수가 뒤바뀌는 것이 핵심입니다!
            new_matrix = [[0] * rows for _ in range(cols)]
            
            for r in range(rows):
                for c in range(cols):
                    # 2. 값 복사: 기존의 '열'이 새로운 '행'이 됩니다.
                    # 기존의 '행'은 뒤집혀서 새로운 '열'이 됩니다.
                    new_matrix[c][(rows - 1) - r] = matrix[r][c]
            
    matrix = new_matrix
            
    return matrix

matrix = [[1,2,3], [4,5,6], [7,8,9]]
commands = ["swapRows 0 1", "swapColumns 0 1", "reverseRow 0", "reverseColumn 0", "rotate90Clockwise"]
# print(solution2(matrix, commands))

def solution3(firstArray, secondArray):
    prefixes = set()
    
    # 1. firstArray의 모든 숫자에서 가능한 모든 접두사를 추출하여 set에 저장
    for num in firstArray:
        s = str(num)
        for i in range(1, len(s) + 1):
            prefixes.add(s[:i])

    max_length = 0
    
    # 2. secondArray의 숫자를 확인하며 set에 있는지 검사
    for num in secondArray:
        s = str(num)
        # 긴 접두사부터 거꾸로 확인하면 더 효율적입니다.
        for i in range(len(s), 0, -1):
            # 현재 찾은 최대 길이보다 짧은 접두사는 검사할 필요가 없음
            if i <= max_length:
                break
                
            if s[:i] in prefixes:
                max_length = max(max_length, i)
                break # 이 숫자에서 가장 긴 접두사를 찾았으므로 다음 숫자로 이동
                
    return max_length

firstArray = [25, 54546]
secondArray = [54547]

# print(solution3(firstArray, secondArray))

a = [1,1,2,3,3,3,3,4,5,6,6]

from collections import Counter

counter = Counter(a)
print(counter)
b = sorted(counter.items(), key=lambda x: (x[1], -x[0]))
print(b)