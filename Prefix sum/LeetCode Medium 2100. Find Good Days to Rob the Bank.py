class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:


        # total length of security on duty days
        days = len(security)

        ## Base case
        if time == 0:

            # Threshold is too small, every day is good day.
            return [ day_i for day_i in range(days) ]


        elif time > days // 2:

            # Threshold is too large, impossible to have good days.
            return []


        ## General case

        # Prefix table, record of length of continuous security guard weakening on index i
        weakenDays = [0] * days
        # Postfix table, record of length of continuous security guard strengthening on index i
        strengthenDays = [0] * days

        # Update prefix table and postfix table
        for i in range(1, days):

            if security[i] <= security[i-1]:
                weakenDays[i] = weakenDays[i-1] + 1

            if security[-i-1] <= security[-i]:
                strengthenDays[-i-1] =  strengthenDays[-i] + 1


        # helper lambda function to judege good day by definition
        is_good_day = lambda i: ( weakenDays[i] >= time ) and ( strengthenDays[i] >= time )

        return [ day_i for day_i in range( days ) if is_good_day(day_i) ]
