from collections import deque

jobs = deque([int(x) for x in input().split(', ')])
jobs_copy = jobs.copy()
index = int(input())
cycles = 0
index_reached = False

while jobs:
    smallest_job = min(jobs)
    if jobs_copy[index] != smallest_job:
        cycles += smallest_job
        jobs.remove(smallest_job)
    else:
        for ind in range(len(jobs_copy)):
            if jobs_copy[ind] == smallest_job and ind == index:
                index_reached = True
                cycles += smallest_job
                break
            elif jobs_copy[ind] == smallest_job and ind != index:
                cycles += smallest_job
                jobs.remove(smallest_job)

    if index_reached:
        break

print(cycles)
