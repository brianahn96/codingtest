class LandManager:
    def __init__(self, matrix):
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0
        self.max_side = 0

    def find_max_square_area(self):
        # Time Complexity: O(R*C) where R is rows and C is columns
        # Space Complexity: O(R*C) for the DP table
        if not self.matrix or not self.matrix[0]:
            return 0

        # DP 테이블 초기화 (원래 행렬과 같은 크기)
        dp = [[0] * self.cols for _ in range(self.rows)]
        
        for i in range(self.rows):
            for j in range(self.cols):
                # 현재 땅이 '좋은 땅(1)'인 경우만 계산
                if self.matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        # 첫 행이나 첫 열은 이전 데이터가 없으므로 자기 자신이 최대 변의 길이
                        dp[i][j] = 1
                    else:
                        # 위, 왼쪽, 대각선 위 중 최솟값 + 1
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    # 전체 행렬에서 가장 큰 변의 길이를 업데이트
                    self.max_side = max(self.max_side, dp[i][j])

        # 넓이(변 * 변) 반환
        return self.max_side ** 2

# 예시 데이터 적용
example_matrix = [
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

manager = LandManager(example_matrix)
result = manager.find_max_square_area()
print(f"최대 정사각형의 넓이: {result}")