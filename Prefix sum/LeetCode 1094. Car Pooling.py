 
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #?
        last_drop=-1
        for i in trips:
            last_drop=max(last_drop,i[2])

        events=[0]*(last_drop+1)
        for pas,st,en in trips:
            events[st]+=pas
            events[en]-=pas
        if events[0]>capacity:
            return False
        for i in range(1,len(events)):
            events[i]=events[i]+events[i-1]
            if events[i]>capacity:
                return False
        return True

