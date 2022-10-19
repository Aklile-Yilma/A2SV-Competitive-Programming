 
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # dictionary containing {letter: last_index_seen}
        last_index = {}

        # create our hash map/dict
        for idx, letter in enumerate(s):
            last_index[letter] = idx



        size, end, result = 0, 0, []

        for idx, letter in enumerate(s):

            size +=1
            # keep track of the max index of a letter in our partition
            end = max(end, last_index[letter])

            # if our current index is known to be the last index of letter
            if (end == idx):
                result.append(size)
                size = 0

        return result








# TIME-COMPLEXITY: O()
# SPACE-COMPLEXITY: O(26) == 0(1)
