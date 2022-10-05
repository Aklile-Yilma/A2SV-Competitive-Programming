 class Solution:
    def slideTheWindow(self, prefix_sum, prefix_sum_len, first_start, first_end, second_start, second_end):
        possible_answer = 0
        first_window_max_sum = 0
        while second_end < prefix_sum_len:
            first_window_cur_sum = prefix_sum[first_end] - prefix_sum[first_start - 1]
            first_window_max_sum = max(first_window_max_sum, first_window_cur_sum)
            second_window_cur_sum = prefix_sum[second_end] - prefix_sum[second_start - 1]
            possible_answer = max(possible_answer, first_window_max_sum + second_window_cur_sum)
            # Update pointers
            first_start += 1
            first_end += 1
            second_start += 1
            second_end += 1

        return possible_answer

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sum = [0] + list(accumulate(nums))

        prefix_sum_len = len(nums) + 1
        first_possible_answer = self.slideTheWindow(prefix_sum, prefix_sum_len, 1, firstLen, firstLen + 1, firstLen + secondLen)
        second_possible_answer = self.slideTheWindow(prefix_sum, prefix_sum_len, 1, secondLen, secondLen + 1, secondLen + firstLen)

        return max(first_possible_answer, second_possible_answer)

