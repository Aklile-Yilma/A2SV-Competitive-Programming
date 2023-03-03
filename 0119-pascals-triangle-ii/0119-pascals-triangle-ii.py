class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        
        before = self.getRow(rowIndex - 1)
        newArr = [1]        
        for idx in range(len(before)-1):
            #sum the new array
            newArr.append(before[idx] + before[idx+1])
        newArr.append(1)
        
        return newArr