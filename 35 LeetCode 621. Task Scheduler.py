class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Least interval is len(tasks) + idle time
        tasks_c = collections.Counter(tasks).most_common()

		# there is no idle time after the last task, so we subtract 1 from max frequency
        idle_time = (tasks_c[0][1]-1) * n

        for i in range(1, len(tasks_c)):
            idle_time -= min(tasks_c[i][1], tasks_c[0][1] - 1)
        idle_time = max(0, idle_time)

        return len(tasks) + idle_time

