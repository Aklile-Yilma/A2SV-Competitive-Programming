class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.vote_count = defaultdict(int) #{person: vote_count}
        self.time_map = {} #{time: person_leading}
        leading = persons[0]
        
        for idx in range(len(persons)):
            curr_person = persons[idx]
            curr_time = times[idx]
            self.vote_count[curr_person] += 1
            
            if self.vote_count[leading] <= self.vote_count[curr_person]:
                leading = curr_person
            
            self.time_map[curr_time] = leading

    def q(self, t: int) -> int:
        
        low = 0
        high = len(self.times) - 1
                
        while low <= high:
            mid = (low + high) // 2
            
            if self.times[mid] < t:
                low = mid + 1
            elif self.times[mid] > t:
                high = mid - 1
            else:
                return self.time_map[self.times[mid]]

        return self.time_map[self.times[high]]
                
            
                


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)