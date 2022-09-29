class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n= len(changed)

        #if size is odd return []
        if (n%2):
            return []

        # dictionary of how many times a value exists in the list
        # key is the value
        # value is the number of times it exists
        count = Counter(changed)
        changed = sorted(changed)
        answer = []

        for num in changed:

            if num==0 and count[num]>=2:
                count[num]-=2
                answer.append(num)

            elif num> 0 and count[num] and count[num*2]:
                count[num] -= 1
                count[num*2] -=1
                answer.append(num)

            return answer if len(answer) == n // 2 else []
                

class Solution:
        # dictionary of how many times a value exists in the list
        # key is the value
        # value is the number of times it exists
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2: return []
        ctr = collections.Counter(changed)
        ans = []
        for val in sorted(changed):
            if val in ctr and val*2 in ctr:
                ctr[val] -= 1
                ctr[val*2] -= 1
                if ctr[val] == 0: del ctr[val]
                if val*2 in ctr and ctr[val*2]==0: del ctr[val*2]
                ans.append(val)
        return [] if len(ctr) else ans








