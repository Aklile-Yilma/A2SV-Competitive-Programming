class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        prefix = [0]

        #calculating the prefix sum
        for num in arr:
            prefix.append(num + prefix[-1])

        left = 0
        #setting k-1 to right b/c left is zero indexed
        right = k-1
        result = 0


        while right < len(arr):

            #calculate current sum
            summation = prefix[right + 1] - prefix[left]
            #calculate current average
            average = summation / k


            if(average >= threshold):
                result +=1

            right +=1
            left +=1

        return result
