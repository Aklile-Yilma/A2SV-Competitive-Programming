class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counter = Counter(words[0])

        for i in range(1, len(words)):
            current_counter = Counter(words[i])
            for char in common_counter:
                common_counter[char] = min(common_counter[char], current_counter[char])

        return common_counter.elements()
        