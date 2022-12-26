class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s_cnt, t_cnt = Counter(s), Counter(t)
        for letter in t_cnt:
            if not s_cnt[letter] == t_cnt[letter]:
                return letter