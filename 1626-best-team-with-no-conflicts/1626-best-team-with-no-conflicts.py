# class Solution:
#     def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
#         n = len(scores)
#         age_score = [(ages[idx], scores[idx]) for idx in range(n)]
#         age_score.sort()

#         dp = {}
#         dp[(n, -1)] = 0
#         max_idx = -1

#         for idx in range(n):
#             print()
#             new_max = max_idx if max_idx != -1 and age_score[idx][1] < age_score[max_idx][1] else idx

#             if max_idx != -1 and age_score[idx][0] > age_score[max_idx][0] and age_score[idx][1] < age_score[max_idx][1]:
#                 dp[(idx, max_idx)] = dp[(idx + 1, max_idx)] if idx+1 < n else 0
#             else:
#                 pick = age_score[idx][1] + dp[(idx+1, new_max)] if idx+1 < n else age_score[idx][1]
#                 not_pick = dp[(idx+1, max_idx)] if idx+1 < n else 0
#                 dp[(idx, max_idx)] = max(pick, not_pick)

#         return dp[(0, max_idx)]

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        pairs = [[scores[i],ages[i]] for i in range(len(scores))]

        pairs.sort()

        dp = [pairs[i][0] for i in range(len(pairs))]

        for i in range(len(pairs)):
            mscore , mage = pairs[i]
            for j in range(0,i):
                score,age = pairs[j]
                if mage>=age:
                    dp[i] = max(mscore+dp[j],dp[i])


        return max(dp)    

# doesn't pass using python
# class Solution:
#     def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
#         n = len(scores)
#         memo = {}
#         age_score = [(ages[idx], scores[idx]) for idx in range(n)]
#         age_score.sort()
        
#         # curr_idx, max_score_idx
#         def dfs(curr_idx, max_idx):
            
#             if curr_idx >= n:
#                 return 0
            
#             if (curr_idx, max_idx) not in memo:
#                 new_max = max_idx if max_idx != -1 and age_score[curr_idx][1] < age_score[max_idx][1] else curr_idx
#                 if max_idx != -1 and age_score[curr_idx][0] > age_score[max_idx][0] and age_score[curr_idx][1] < age_score[max_idx][1]:
#                     # cann't add curr
#                     memo[(curr_idx, max_idx)] = dfs(curr_idx+1, max_idx)
#                 else:
#                     #not pick or pick
#                     memo[(curr_idx, max_idx)] = max(dfs(curr_idx+1, max_idx), age_score[curr_idx][1] + dfs(curr_idx+1, new_max))

#             return memo[(curr_idx, max_idx)]
            
#         return dfs(0, -1)