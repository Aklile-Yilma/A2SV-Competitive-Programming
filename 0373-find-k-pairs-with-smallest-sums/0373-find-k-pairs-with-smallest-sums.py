class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []
        len1 = len(nums1)
        len2 = len(nums2)
        
        for idx in range(len2):
            total = nums1[0] + nums2[idx]
            heappush(heap, (total, [nums1[0], nums2[idx]], 0, idx))
        answer = []
        for _ in range(k):
            if not heap:
                break
            total, pair, row, col = heappop(heap)
            answer.append(pair)
            

            if row + 1 < len(nums1):
                total = nums1[row+1] + nums2[col] 
                heappush(heap, (total, [nums1[row+1], nums2[col]], row+1, col))

        return answer
        