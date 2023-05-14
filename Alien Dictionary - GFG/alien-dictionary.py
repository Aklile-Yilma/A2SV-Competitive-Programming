#User function Template for python3
from collections import defaultdict, deque

class Solution:
    def findOrder(self, alien_dict, N, K):
        # code here
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for curr in range(1, N):
            ltrPtr = 0
            prev = curr-1
            max_size = min(len(alien_dict[prev]), len(alien_dict[curr]))
            while ltrPtr < max_size and alien_dict[prev][ltrPtr] == alien_dict[curr][ltrPtr]:
                ltrPtr += 1

            if ltrPtr < max_size:
                parent = alien_dict[prev][ltrPtr]
                child = alien_dict[curr][ltrPtr]
                graph[parent].append(child)
                indegree[child] += 1
                
        q = deque()
        #append independent nodes to the q
        for idx in range(k):
            letter = chr(97+idx)
            if indegree[letter] == 0:
                q.append(letter)
                
        order = []
        while q:
            letter = q.popleft()
            order.append(letter)

            for child in graph[letter]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
                    
        
        return "".join(order)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends