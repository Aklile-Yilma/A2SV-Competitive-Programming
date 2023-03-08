class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def findFreqOfSmallest(word):
            word = sorted(word)
            count = Counter(word)
            
            return count[word[0]]
        
        count_query = []
        for query in queries:
            count = findFreqOfSmallest(query)
            count_query.append(count)
            
        count_words = []
        for word in words:
            count = findFreqOfSmallest(word)
            count_words.append(count)
        
        #sort words count
        count_words.sort()
        answer = []
        
        for query in count_query:
            low = 0 
            high = len(count_words) - 1

            while low <= high:
                mid = (low + high) // 2

                if count_words[mid] > query:
                    high = mid - 1
                elif count_words[mid] <= query:
                    low = mid + 1
                                
            answer.append(len(count_words) - low)
            
                    
        return answer
                    
            
        
            
        

# class Solution:
#     def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
#         def findFreqOfSmallest(word):
#             word = sorted(word)
#             count = Counter(word)
            
#             return count[word[0]]
            
#         answer = []
        
#         for query in queries:
#             count = 0
#             count_query = findFreqOfSmallest(query)
            
#             for word in words:
#                 count_word = findFreqOfSmallest(word)
                
#                 if count_query < count_word:
#                     count += 1
                
#             answer.append(count)
            
#         return answer
                
                
            
            
        