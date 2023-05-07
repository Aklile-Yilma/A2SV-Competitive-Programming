class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        row_len, col_len = len(matrix), len(matrix[0])
        heap = []
        for row in range(row_len):
            for col in range(col_len):
                heappush(heap, matrix[row][col])
        
        answer = -1
        for _ in range(k):
            answer = heappop(heap)
            
        return answer