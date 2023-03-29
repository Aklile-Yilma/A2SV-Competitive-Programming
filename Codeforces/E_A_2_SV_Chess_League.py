class A2sv_chess_league:
    
    def mergeSort(self, left, right, arr):
        
        if left == right:
            return [arr[left]]
        
        mid = left + (right - left) // 2
        left_half = self.mergeSort(left, mid, arr)
        right_half = self.mergeSort(mid + 1, right, arr)
        
        self.checkWinners(left_half, right_half)
        return self.merge(left_half, right_half)


    def merge(self,arr1, arr2):

        arr1_pointer = 0
        arr2_pointer = 0
        arr3 = []
        idx = 0
        
        
        while arr1_pointer < len(arr1) and arr2_pointer < len(arr2):
            if arr1[arr1_pointer][0] <= arr2[arr2_pointer][0]:
                arr3.append(arr1[arr1_pointer])
                arr1_pointer += 1
            else:
                arr3.append(arr2[arr2_pointer])
                arr2_pointer += 1
            idx += 1
            
        arr3 += arr1[arr1_pointer:]
        arr3 += arr2[arr2_pointer:]
        
        return arr3
    
    def checkWinners(self, left_half, right_half):
        #check for losers in the left half
        least_in_right = None
        for idx in range(len(right_half)):
            rating, curr_idx, canWin = right_half[idx]
            if canWin:
                least_in_right = right_half[idx]
                break
        
        for idx in range(len(left_half)):
            rating, curr_idx, canWin = left_half[idx]
            if not canWin:
                continue
            if least_in_right and left_half[idx][0] + max_diff < least_in_right[0]: 
                left_half[idx] = (rating, curr_idx, False)
                
                
        #check for losers in the right half
        
        least_in_left = None
        for idx in range(len(left_half)):
            rating, curr_idx, canWin = left_half[idx]
            if canWin:
                least_in_left = left_half[idx]
                break
        
        for idx in range(len(right_half)):
            rating, curr_idx, canWin = right_half[idx]
            if not canWin:
                continue
            if least_in_left and right_half[idx][0] + max_diff < least_in_left[0]: 
                right_half[idx] = (rating, curr_idx, False)
                
        return
        

num_rounds, max_diff = list(map(int, input().split()))
ratings = list(map(int, input().split()))

# format rating
players = []

for idx in range(len(ratings)):
    players.append((ratings[idx], idx + 1, True))

s = A2sv_chess_league()
players = s.mergeSort(0, len(players)-1, players)

result = []

for rating, idx, canWin in players:
    if canWin:
        result.append(idx)
        
result.sort()
print(*result)
