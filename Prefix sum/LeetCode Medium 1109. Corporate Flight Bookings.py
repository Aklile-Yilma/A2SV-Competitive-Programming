 
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        #?

        res = [0] * n
        for first, last, seats in bookings:
			# 1-based index
            # Simply store changes at the borders of the ranges of each
            res[first-1] += seats
            if last < n:
                res[last] -= seats

        print(res)
        # Take the cumulative sum of the entire array
        for i in range(1, n):
            res[i] += res[i-1]
        return res


    #BRUTE FORCE
#         result = [0] * n

#         for

#         for item in bookings:
#             start_idx = item[0] - 1
#             last_idx = item[1] - 1
#             seats = item[2]

# #             while start_idx <= last_idx:
# #                 result[start_idx] += seats
# #                 start_idx += 1

#         return result
